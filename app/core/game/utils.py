import random
from typing import Optional

from django.db.models.query import QuerySet

from app.core.game.models import Category, Game, Question
from app.core.game.serializers import QuestionSerializer
from app.core.user_profile.models import Profile


def generate_game(label: str, author: Optional[Profile] = None) -> list:
    category_ids: list = [
        cat.id for cat in Category.objects.all() if cat.question_set.count() > 3
    ]
    random_category_ids: list = random.sample(category_ids, 6)
    randoms_categories: QuerySet[Category] = Category.objects.filter(
        id__in=random_category_ids
    )

    new_game = Game.objects.create(label=label)
    if author:
        new_game.author = author
        new_game.save()

    questions = []
    for category in randoms_categories:
        question_ids = [
            question.id for question in Question.objects.filter(category=category)
        ]
        random_count = random.randint(5, 8)
        random_question_ids: list = random.sample(question_ids, random_count)
        randoms_questions: QuestionSerializer = QuestionSerializer(
            data=Question.objects.filter(id__in=random_question_ids), many=True
        )
        randoms_questions.is_valid()

        questions.append(
            {"category": category.label, "questions": randoms_questions.data}
        )

    return questions
