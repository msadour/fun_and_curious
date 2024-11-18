import re
from typing import Any, Optional

from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.http import QueryDict
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from app.core.user_profile.models import Profile
from app.layer.exception import (
    AuthenticationError,
    EmailError,
    PasswordError,
    ProfileAlreadyExistsError,
    UsernameError,
)


class AuthTokenSerializer(serializers.Serializer):

    username: serializers.CharField = serializers.CharField()
    password: serializers.CharField = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def authenticate_user(
        self, username: str = None, email: str = None, password: str = None
    ) -> Optional[Profile]:
        profile = Profile.objects.filter(Q(username=username) | Q(email=email)).first()

        if profile is None:
            raise AuthenticationError("Not user found with this username/email.")

        if not profile.is_active:
            raise AuthenticationError("This account is deactivate.")

        if not check_password(password, profile.password):
            raise AuthenticationError("Username/Password doesn't match.")

        return profile

    def validate(self, attrs: Any) -> Profile:
        if isinstance(attrs, QueryDict):
            attrs = attrs.dict()

        username: str = attrs.get("username")
        email: str = attrs.get("email")
        password: str = attrs.get("password")
        profile: Optional[Profile] = self.authenticate_user(
            username=username, email=email, password=password
        )
        token, created = Token.objects.get_or_create(user=profile)
        profile.auth_token = token

        return profile


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data.get("email")
        if email is None or email == "":
            raise EmailError(message="Email cannot be empty")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
            raise EmailError(message="Email must have a valid format (XXX@YYY.com)")

        username = validated_data.get("username")
        if username is None or len(username) < 3:
            raise UsernameError("Username is too short (at least 3 letters)")

        check_existing_profile = Profile.objects.filter(
            Q(username=username) | Q(email=email)
        ).first()
        if check_existing_profile:
            raise ProfileAlreadyExistsError(
                "A profile with this email/username already exists"
            )

        password = validated_data.get("password")
        if password is None or len(password) < 5:
            raise PasswordError("Password should at least contains 5 characters")

        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        country = validated_data.get("country")
        city = validated_data.get("city")

        profile = Profile.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            country=country,
            city=city,
        )

        return profile
