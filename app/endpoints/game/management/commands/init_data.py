from django.core.management import BaseCommand, call_command

from app.endpoints.question.models import Category, Question


class Command(BaseCommand):
    help = "Marks the specified blog post as published."

    def handle(self, *args, **options):
        Question.objects.all().delete()
        Category.objects.all().delete()

        call_command("loaddata", "./fixtures/category.json")
        call_command("loaddata", "./fixtures/question_animals.json")
        call_command("loaddata", "./fixtures/question_clothes_men.json")
        call_command("loaddata", "./fixtures/question_clothes_women.json")
        call_command("loaddata", "./fixtures/question_gastronomy.json")
        call_command("loaddata", "./fixtures/question_hobbies.json")
        call_command("loaddata", "./fixtures/question_love.json")
        call_command("loaddata", "./fixtures/question_object.json")
        call_command("loaddata", "./fixtures/question_personality.json")
        call_command("loaddata", "./fixtures/question_polemic.json")
        call_command("loaddata", "./fixtures/question_sport.json")
        call_command("loaddata", "./fixtures/question_travel.json")
        call_command("loaddata", "./fixtures/users.json")
