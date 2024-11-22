from app.layer.exception import (
    AuthenticationError,
    EmailError,
    PasswordError,
    ProfileAlreadyExistsError,
    UsernameError,
)

EXCEPTIONS_HANDLING_MIDDLEWARE = (
    AuthenticationError,
    EmailError,
    UsernameError,
    ProfileAlreadyExistsError,
    PasswordError,
)

LANGUAGES_TRANSLATION_AVAILABLE = ["en", "de"]

URL_BREVO = "https://api.brevo.com/v3/smtp/email"
