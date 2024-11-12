from rest_framework import viewsets
from rest_framework.response import Response

from app.core.game.serializers import GameSerializer
from app.layer.utils import build_response, create_pdf


class RandomQuestionsViewSet(viewsets.ViewSet):
    serializer_class = GameSerializer

    def create(self, request):
        author = None if request.user.is_anonymous else request.user
        label: str = request.data.get("label")
        gender: str = request.data.get("gender")
        only_soft: bool = request.data.get("only_soft")
        language: str = request.data.get("language")
        format_game: str = request.data.get("format_game")

        game_created = self.serializer_class().create(
            validated_data={
                "label": label,
                "author": author,
                "gender": gender,
                "only_soft": only_soft,
                "language": language,
            }
        )

        game_data = GameSerializer(game_created).data
        if format_game == "JSON":
            return Response(data=game_data)

        file_name = game_created.file_name
        create_pdf(
            request=request,
            data={"games": [game_data]},
            template="game/games.html",
            file_name=file_name,
        )

        return build_response(file_name=file_name)
