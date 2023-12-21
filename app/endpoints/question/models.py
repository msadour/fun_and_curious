from django.db import models


class Category(models.Model):
    label = models.CharField(max_length=255, null=False, blank=False)

    objects = models.Manager()


class Question(models.Model):
    label = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = models.Manager()
