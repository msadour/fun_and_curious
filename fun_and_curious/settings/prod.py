from fun_and_curious.settings.base import BASE_DIR

# class Prod(Base):
DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}