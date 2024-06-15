import os

from django.conf import settings
from django.http import Http404, HttpResponse
from rest_framework import viewsets
from rest_framework.request import Request

from app.core.game.utils import generate_game
from app.layer.utils import create_pdf


class RandomQuestionsViewSet(viewsets.ViewSet):
    def create(self, request: Request) -> HttpResponse:
        current_user = request.user
        label: str = request.data.get("label")
        gender: str = request.data.get("gender")

        game_created = (
            generate_game(label=label, gender=gender)
            if current_user.is_anonymous
            else generate_game(label=label, author=current_user, gender=gender)
        )
        create_pdf(
            request,
            data={"games": game_created, "label": label},
            template="game/game.html",
        )

        url_file = str(settings.BASE_DIR) + "\\result.pdf"
        if not os.path.exists(url_file):
            raise Http404
        else:
            with open(url_file, "rb") as fh:
                response = HttpResponse(
                    fh.read(), content_type="application/vnd.ms-excel"
                )
                response[
                    "Content-Disposition"
                ] = "inline; filename=" + os.path.basename(url_file)
            os.remove(url_file)
            return response
