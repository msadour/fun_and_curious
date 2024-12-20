from rest_framework import viewsets
from rest_framework.response import Response

from app.core.game.serializers import GameSerializer
from app.layer.external_libs.mailing import EmailSender
from app.layer.external_libs.pdf import build_response_with_pdf, create_pdf


class RandomQuestionsViewSet(viewsets.ViewSet):
    serializer_class = GameSerializer

    def create(self, request):
        author = None if request.user.is_anonymous else request.user
        label: str = request.data.get("label")
        gender: str = request.data.get("gender")
        only_soft: bool = request.data.get("only_soft")
        language: str = request.data.get("language")

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
        return Response(data=game_data)


class RandomQuestionsPDFViewSet(viewsets.ViewSet):
    serializer_class = GameSerializer

    def create(self, request):
        author = None if request.user.is_anonymous else request.user
        label: str = request.data.get("label")
        gender: str = request.data.get("gender")
        only_soft: bool = request.data.get("only_soft")
        language: str = request.data.get("language")

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
        file_name = game_created.file_name
        create_pdf(
            request=request,
            data={"games": [game_data]},
            template="game/games.html",
            file_name=file_name,
        )
        return build_response_with_pdf(file_name=file_name)


class RandomQuestionsEmailViewSet(viewsets.ViewSet):
    serializer_class = GameSerializer

    def create(self, request):
        author = None if request.user.is_anonymous else request.user
        label: str = request.data.get("label")
        gender: str = request.data.get("gender")
        only_soft: bool = request.data.get("only_soft")
        language: str = request.data.get("language")
        email: str = request.data.get("email")

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
        sender = EmailSender(
            to_email=email,
            game_data=game_data,
            request=request,
            template="game/games_as_email.html",
        )
        sender.send()
        return Response(
            status=200,
            data={"Message": f"Your game was sent on the following email : {email}"},
        )
