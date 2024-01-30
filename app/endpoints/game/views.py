from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from app.endpoints.game.utils import generate_game


class RandomQuestionsViewSet(viewsets.ViewSet):
    def create(self, request: Request) -> Response:
        current_user = request.user
        label: str = request.data.get("label")
        game_created = (
            generate_game(label=label)
            if current_user.is_anonymous
            else generate_game(label=label, author=current_user)
        )
        return Response(data=game_created, status=status.HTTP_201_CREATED)
