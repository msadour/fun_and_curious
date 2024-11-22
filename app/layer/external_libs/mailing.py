import requests
from django.shortcuts import render
from rest_framework.request import Request

from app.layer.constants import URL_BREVO
from app.layer.exception import EmailError
from fun_and_curious.settings import BREVO_MAIL_API_KEY


class EmailSender:
    def __init__(self, to_email: str, game_data: dict, request: Request, template: str):
        self.headers = {
            "content-type": "application/json",
            "accept": "application/json",
            "api-key": BREVO_MAIL_API_KEY,
        }
        self.to_email = to_email
        self.request = request
        html_game = render(request, template, {"games": [game_data]}).content.decode()
        self.email_data = {
            "sender": {"name": "Mehdi", "email": "sadour.mehdi@gmail.com"},
            "to": [{"email": to_email}],
            "subject": "Your game is ready",
            "htmlContent": html_game,
        }

    def send(self):
        try:
            requests.post(url=URL_BREVO, headers=self.headers, json=self.email_data)
        except EmailError as e:
            raise EmailError(message=e.message)
