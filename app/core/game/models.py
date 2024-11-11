import random
import uuid
from typing import Optional

from django.db import models
from django.db.models import Count
from django.db.models.query import QuerySet

from app.core.user_profile.models import Profile


class Gender(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"


class Category(models.Model):
    label = models.CharField(max_length=255, null=False, blank=False)
    gender = models.CharField(max_length=255, choices=Gender.choices, null=True)

    objects = models.Manager()

    def get_filtered_random_question_ids(self, only_soft: bool) -> list:
        question_ids = self.questions.all().values_list("id", flat=True)
        if only_soft and only_soft is True:
            question_ids = question_ids.exclude(is_soft=False)
        question_ids = sorted(question_ids)
        minimum_number_questions = 4 if len(question_ids) >= 4 else len(question_ids)
        random_length = random.randint(minimum_number_questions, 8)
        random_question_ids: list = random.sample(question_ids, random_length)
        return random_question_ids


class Question(models.Model):
    label = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="questions"
    )
    is_soft = models.BooleanField(default=True)

    objects = models.Manager()


class Game(models.Model):
    label = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, related_name="games"
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.JSONField(default=dict)

    objects = models.Manager()

    @property
    def created_at_as_text(self):
        return (
            f'Created the {self.created_at.date().strftime("%d/%m/%Y")} a'
            f't {self.created_at.time().strftime("%H:%M")}'
        )

    @property
    def file_name(self):
        return f"{uuid.uuid4().hex}.pdf"

    @staticmethod
    def get_random_categories(gender: str = None) -> QuerySet[Category]:
        categories = Category.objects.annotate(
            total_questions=Count("questions")
        ).filter(total_questions__gte=5)
        if gender == "Male":
            categories = categories.exclude(gender="Female")
        elif gender == "Female":
            categories = categories.exclude(gender="Male")

        category_ids: list = sorted(categories.values_list("id", flat=True))
        random_category_ids: list = random.choices(category_ids, k=6)

        randoms_categories: QuerySet[Category] = Category.objects.filter(
            id__in=random_category_ids
        )
        return randoms_categories

    def generate_content(
        self, gender: Optional[str] = None, only_soft: bool = True, language: str = None
    ):
        randoms_categories: QuerySet[Category] = self.get_random_categories(
            gender=gender
        )
        questions = []
        for category in randoms_categories:
            random_question_ids = category.get_filtered_random_question_ids(
                only_soft=only_soft
            )
            category_label = category.label
            randoms_questions = Question.objects.filter(id__in=random_question_ids)

            if language:
                if language == "de":
                    category_label = category.label_de
                elif language == "fr":
                    category_label = category.label_fr

                randoms_questions = randoms_questions.values("id", f"label_{language}")
            else:
                category_label = category.label
                randoms_questions = randoms_questions.values("id", "label")

            questions.append(
                {"category": category_label, "questions": list(randoms_questions)}
            )

        self.content = questions
        self.save()


class QuestionCategoryGame(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    objects = models.Manager()
