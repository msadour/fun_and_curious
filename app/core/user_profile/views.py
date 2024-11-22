from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.core.game.models import Game
from app.core.game.serializers import GameSerializer
from app.core.user_profile.models import Profile
from app.core.user_profile.serializers import ProfileListSerializer, ProfileSerializer
from app.layer.external_libs.pdf import build_response_with_pdf, create_pdf


class ManageProfileViewSet(viewsets.ViewSet):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Profile.objects.exclude(is_staff=True)

    def patch(self, request):
        current_user = request.user
        data = request.data
        ProfileSerializer().update(instance=current_user, validated_data=data)
        return Response(status=status.HTTP_200_OK)

    def list(self, request):
        profiles = ProfileListSerializer(self.queryset, many=True).data
        return Response(data=profiles, status=status.HTTP_200_OK)

    def delete(self, request):
        Profile.objects.filter(id=request.user.id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameProfileViewSet(viewsets.ViewSet):
    permission_classes = [
        IsAuthenticated,
    ]

    def list(self, request):
        games_filtered = Game.objects.filter(author=request.user)
        games = GameSerializer(games_filtered, many=True).data
        file_name = "my_games.pdf"
        create_pdf(
            request=request,
            data={"games": games},
            template="game/games.html",
            file_name=file_name,
        )
        return build_response_with_pdf(file_name=file_name)
