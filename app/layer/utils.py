from typing import Dict

import pdfkit
from django.shortcuts import render
from rest_framework.request import Request


def create_pdf(request: Request, data: dict, template: str) -> Dict:
    html_game = render(request, template, data).content.decode()
    file_name = "result.pdf"
    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe"
    )
    pdfkit.from_string(html_game, file_name, configuration=config)
    return {"file_name": file_name}
