import re

from rest_framework import serializers

from app.core.user_profile.models import Profile
from app.layer.exception import EmailError, UsernameError


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ("id", "email", "password", "is_staff", "groups", "user_permissions")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def update(self, instance: Profile, validated_data: dict):
        email = validated_data.get("email")
        if email and email != instance.email:
            if (
                Profile.objects.exclude(email=instance.email)
                .filter(email=email)
                .exists()
            ):
                raise EmailError(message="This email is token")
            if re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
                raise EmailError(message="Email must have a valid format (XXX@YYY.com)")
            instance.email = email

        username = validated_data.get("username")
        if username and username != instance.username:
            if Profile.objects.filter(username=username).exists():
                raise UsernameError(message="This username is token")
            if len(username) < 3:
                raise UsernameError("Username is too short (at least 3 letters)")
            instance.username = username

        first_name = validated_data.get("first_name")
        if first_name:
            instance.first_name = first_name

        last_name = validated_data.get("last_name")
        if last_name:
            instance.first_name = last_name

        country = validated_data.get("country")
        if country:
            instance.country = country

        city = validated_data.get("city")
        if city:
            instance.city = city

        instance.save()
        return instance
