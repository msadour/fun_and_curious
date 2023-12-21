from typing import Any, Optional

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import QueryDict
from django.db.models import Q
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from app.endpoints.user_profile.models import Profile
from app.layer.exception import AuthenticationError


class AuthTokenSerializer(serializers.Serializer):

    username: serializers.CharField = serializers.CharField()
    password: serializers.CharField = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def authenticate_user(
        self, username: str = None, email: str = None, password: str = None
    ) -> Optional[Profile]:
        profile: Profile = Profile.objects.filter(Q(username=username) | Q(email=email)).first()

        if profile is None:
            raise AuthenticationError("Not user found with this username/email.")

        if not profile.is_active:
            raise AuthenticationError("This account is deactivate.")

        if not check_password(password, profile.password):
            raise AuthenticationError("Username/Password doesn't match.")

        return profile

    def validate(self, attrs: Any) -> Profile:
        if type(attrs) == QueryDict:
            attrs = attrs.dict()

        username: str = attrs.get("username")
        email: str = attrs.get("email")
        password: str = attrs.get("password")
        profile: Optional[Profile] = self.authenticate_user(username=username, email=email, password=password)
        token, created = Token.objects.get_or_create(user=profile)
        profile.auth_token = token

        return profile
