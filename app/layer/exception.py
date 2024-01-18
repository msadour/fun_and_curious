class AuthenticationError(Exception):
    def __init__(self, message):
        self.message = message
        self.code = 400
        super().__init__(self.message)


class EmailError(Exception):
    def __init__(self, message):
        self.message = message
        self.code = 400
        super().__init__(self.message)


class UsernameError(Exception):
    def __init__(self, message):
        self.message = message
        self.code = 400
        super().__init__(self.message)


class ProfileAlreadyExistsError(Exception):
    def __init__(self, message):
        self.message = message
        self.code = 400
        super().__init__(self.message)


class PasswordError(Exception):
    def __init__(self, message):
        self.message = message
        self.code = 400
        super().__init__(self.message)
