from rest_framework import viewsets
from rest_framework.response import Response

from app.core.game.serializers import GameSerializer
from app.layer.email_sending import EmailSender
from app.layer.pdf import build_response_with_pdf, create_pdf


class RandomQuestionsViewSet(viewsets.ViewSet):
    serializer_class = GameSerializer

    def create(self, request):
        author = None if request.user.is_anonymous else request.user
        label: str = request.data.get("label")
        gender: str = request.data.get("gender")
        only_soft: bool = request.data.get("only_soft")
        language: str = request.data.get("language")
        format_response: str = request.data.get("format_response")
        to_email: str = request.data.get("to_email")

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
        if format_response == "email":
            sender = EmailSender(
                to_email=to_email,
                game_data=game_data,
                request=request,
                template="game/games_as_email.html",
            )
            sender.send()
            return Response(
                status=200,
                data={
                    "Message": f"Your game was sent on the following email : {to_email}"
                },
            )
        elif format_response == "pdf":
            create_pdf(
                request=request,
                data={"games": [game_data]},
                template="game/games.html",
                file_name=file_name,
            )
            return build_response_with_pdf(file_name=file_name)
        else:
            return Response(data=game_data)
