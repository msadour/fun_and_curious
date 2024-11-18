import os

from django.conf import settings


def get_url_file(file_name: str):
    url_file = os.path.join(str(settings.BASE_DIR), file_name)
    if not os.path.exists(url_file):
        url_file_in_pythonanywhere_console = os.path.join(
            str(settings.BASE_DIR.parent), file_name
        )
        if not os.path.exists(url_file_in_pythonanywhere_console):
            raise OSError("File not found")
        url_file = url_file_in_pythonanywhere_console

    return url_file


def remove_pdf_file(file_name: str):
    url_file = get_url_file(file_name)
    os.remove(url_file)
