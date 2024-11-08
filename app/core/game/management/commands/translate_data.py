from deep_translator import GoogleTranslator
from django.core.management import BaseCommand

from app.core.game.models import Category, Question


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = Category.objects.all()
        for category in categories:
            category_de = GoogleTranslator(source="auto", target="de").translate(
                category.label
            )
            category.label_de = category_de

            category_fr = GoogleTranslator(source="auto", target="fr").translate(
                category.label
            )
            category.label_fr = category_fr

            category.save()

        questions = Question.objects.all()
        for question in questions:
            question_de = GoogleTranslator(source="auto", target="de").translate(
                question.label
            )
            question.label_de = question_de

            question_fr = GoogleTranslator(source="auto", target="fr").translate(
                question.label
            )
            question.label_fr = question_fr

            question.save()
