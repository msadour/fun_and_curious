import random
from typing import Optional

from django.db.models.query import QuerySet

from app.endpoints.game.models import Game, QuestionCategoryGame
from app.endpoints.question.models import Category, Question
from app.endpoints.question.serializers import QuestionSerializer
from app.endpoints.user_profile.models import Profile


def generate_default_game(label: str, author: Optional[Profile] = None) -> list:

    category_ids: list = [
        cat.id for cat in Category.objects.all() if cat.question_set.count() > 3
    ]
    random_category_ids: list = random.sample(category_ids, 4)
    randoms_categories: QuerySet[Category] = Category.objects.filter(
        id__in=random_category_ids
    )

    new_game = Game.objects.create(label=label)
    if author:
        new_game.author = author
        new_game.save()

    questions: list = []
    for category in randoms_categories:
        question_ids: list = []
        for question in Question.objects.filter(category=category):
            question_ids.append(question.id)
            QuestionCategoryGame.objects.create(
                question=question,
                category=category,
                game=new_game,
            )

        question_ids: list = [
            question.id for question in Question.objects.filter(category=category)
        ]
        length_question_ids: int = len(question_ids)

        if length_question_ids > 10:
            random_count = random.randint(3, 7)
            random_question_ids: list = random.sample(question_ids, random_count)
        else:
            random_count = random.randint(1, length_question_ids)
            random_question_ids: list = random.sample(question_ids, random_count)

        randoms_questions: QuestionSerializer = QuestionSerializer(
            data=Question.objects.filter(id__in=random_question_ids), many=True
        )
        randoms_questions.is_valid()
        questions.append(
            {"category": category.label, "questions": randoms_questions.data}
        )

    return questions
