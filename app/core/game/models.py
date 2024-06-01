from django.db import models

from app.core.user_profile.models import Profile


class Category(models.Model):
    label = models.CharField(max_length=255, null=False, blank=False)

    objects = models.Manager()


class Question(models.Model):
    label = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = models.Manager()


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
