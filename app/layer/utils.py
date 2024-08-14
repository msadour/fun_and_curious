import os
from typing import Dict

import pdfkit
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.request import Request


def create_pdf(request: Request, data: dict, template: str, file_name: str) -> Dict:
    html_game = render(request, template, data).content.decode()
    config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_PATH)
    pdfkit.from_string(html_game, file_name, configuration=config)
    return {"file_name": file_name}


def build_response(file_name: str) -> HttpResponse:
    url_file = os.path.join(str(settings.BASE_DIR), file_name)
    if not os.path.exists(url_file):
        url_file_in_pythonanywhere_console = os.path.join(
            str(settings.BASE_DIR.parent), file_name
        )
        if not os.path.exists(url_file_in_pythonanywhere_console):
            raise OSError("File not found")
        url_file = url_file_in_pythonanywhere_console

    with open(url_file, "rb") as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response["Content-Disposition"] = "inline; filename=" + os.path.basename(
            url_file
        )
    os.remove(url_file)

    return response
