import os

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME", "test_db"),
        "USER": os.environ.get("DB_USER", "test_user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "test_password"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
        "TEST": {
            "NAME": "fun_and_curious",
        },
    }
}

WKHTMLTOPDF_PATH = os.path.join(
    "C:\\", "Program Files", "wkhtmltopdf", "bin", "wkhtmltopdf.exe"
)
