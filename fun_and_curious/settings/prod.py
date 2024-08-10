from fun_and_curious.settings.base import BASE_DIR

# class Prod(Base):
DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

WKHTMLTOPDF_PATH = "/home/msadr/wkhtmltopdf-0.12.5/src/pdf/wkhtmltopdf.cc"
