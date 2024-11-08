from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from app.core.game.models import Category, Question


@admin.register(Question)
class QuestionAdmin(TranslationAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass
