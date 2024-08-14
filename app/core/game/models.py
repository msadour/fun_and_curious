import uuid

from django.db import models

from app.core.user_profile.models import Profile


class Gender(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"


class Category(models.Model):
    label = models.CharField(max_length=255, null=False, blank=False)
    gender = models.CharField(max_length=255, choices=Gender.choices, null=True)

    objects = models.Manager()


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
    def file_name(self):
        return f"{uuid.uuid4().hex}.pdf"


class QuestionCategoryGame(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    objects = models.Manager()
