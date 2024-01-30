from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from app.endpoints.game.utils import generate_default_game


class RandomQuestionsViewSet(viewsets.ViewSet):
    def create(self, request: Request) -> Response:
        current_user = request.user
        label: str = request.data.get("label")
        if current_user.is_anonymous:
            data: list = generate_default_game(label=label)
        else:
            data: list = generate_default_game(label=label, author=current_user)
        return Response(data=data, status=status.HTTP_201_CREATED)
