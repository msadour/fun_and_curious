from django.db import models

from app.endpoints.question.models import Question, Category
from app.endpoints.user_profile.models import Profile


class Game(models.Model):
    label = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    objects = models.Manager()


class QuestionCategoryGame(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    objects = models.Manager()
