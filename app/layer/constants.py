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
