from modeltranslation.translator import TranslationOptions, register

from .models import Category, Question


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ("label",)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("label",)
