import sib_api_v3_sdk
from django.shortcuts import render
from rest_framework.request import Request

from app.layer.exception import EmailError
from fun_and_curious.settings import BREVO_MAIL_API_KEY


class EmailSender:
    def __init__(self, to_email: str, game_data: dict, request: Request, template: str):
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
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key["api-key"] = BREVO_MAIL_API_KEY
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(configuration)
        )

        try:
            api_instance.send_transac_email(self.email_data)
        except EmailError as e:
            raise EmailError(message=e.message)
