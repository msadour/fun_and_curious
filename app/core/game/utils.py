import random
from typing import Optional

from django.db.models import Count
from django.db.models.query import QuerySet

from app.core.game.models import Category, Game, Question
from app.core.game.serializers import QuestionSerializer
from app.core.user_profile.models import Profile


def get_random_categories(gender: str = None) -> QuerySet[Category]:
    categories = Category.objects.annotate(total_questions=Count("questions")).filter(
        total_questions__gte=5
    )
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


def create_game(label: str, questions: list, author: Optional[Profile] = None) -> Game:
    new_game = Game.objects.create(label=label)
    if author:
        new_game.author = author
    new_game.content = questions
    new_game.save()
    return new_game


def get_filtered_random_question_ids(category: Category, only_soft: bool) -> list:
    question_ids = Question.objects.filter(category=category).values_list(
        "id", flat=True
    )
    if only_soft and only_soft is True:
        question_ids = question_ids.exclude(is_soft=False)
    question_ids = sorted(question_ids)
    minimum_number_questions = 4 if len(question_ids) >= 4 else len(question_ids)
    random_length = random.randint(minimum_number_questions, 8)
    random_question_ids: list = random.sample(question_ids, random_length)
    return random_question_ids


def generate_game(
    label: str,
    author: Optional[Profile] = None,
    gender: Optional[str] = None,
    only_soft: bool = True,
) -> Game:
    randoms_categories: QuerySet[Category] = get_random_categories(gender=gender)
    questions = []
    for category in randoms_categories:
        random_question_ids = get_filtered_random_question_ids(
            category=category, only_soft=only_soft
        )
        randoms_questions: QuestionSerializer = QuestionSerializer(
            data=Question.objects.filter(id__in=random_question_ids), many=True
        )
        randoms_questions.is_valid()
        questions.append(
            {"category": category.label, "questions": randoms_questions.data}
        )

    new_game = create_game(label=label, author=author, questions=questions)

    return new_game
