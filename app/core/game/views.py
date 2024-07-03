from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.request import Request

from app.core.game.serializers import GameSerializer
from app.core.game.utils import generate_game
from app.layer.utils import build_response, create_pdf


class RandomQuestionsViewSet(viewsets.ViewSet):
    def create(self, request: Request) -> HttpResponse:
        author = None if request.user.is_anonymous else request.user
        label: str = request.data.get("label")
        gender: str = request.data.get("gender")

        game_created = generate_game(label=label, author=author, gender=gender)
        game_data = GameSerializer(game_created).data
        file_name = "game_created.pdf"
        create_pdf(
            request=request,
            data={"games": [game_data]},
            template="game/games.html",
            file_name=file_name,
        )
        return build_response(file_name=file_name)
