from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from app.endpoints.game.utils import generate_default_game
from app.endpoints.user_profile.models import Profile


class RandomQuestionsViewSet(viewsets.ViewSet):

    def create(self, request: Request) -> Response:
        current_user: Profile = Profile.objects.filter(id=request.user.id).first()
        label: str = request.data.get("label")
        data: list = generate_default_game(label=label, author=current_user)
        return Response(data=data, status=status.HTTP_201_CREATED)
