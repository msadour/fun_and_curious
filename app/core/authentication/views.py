from django.contrib.auth import logout as django_logout
from django.contrib.auth.base_user import AbstractBaseUser
from rest_framework import permissions, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from app.core.authentication.serializers import AuthTokenSerializer, SignUpSerializer


class SignUpViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs) -> Response:
        SignUpSerializer().create(validated_data=request.data)
        return Response(
            data={"message": "Account created"}, status=status.HTTP_201_CREATED
        )


class CustomAuthTokenView(ObtainAuthToken):

    authentication_classes: tuple = (TokenAuthentication,)
    permission_classes: tuple = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs) -> Response:
        serializer = AuthTokenSerializer()
        user_logged: AbstractBaseUser = serializer.validate(attrs=request.data)
        request.user = user_logged
        return Response(data={"token": request.user.auth_token.key}, status=201)


class LogoutViewSet(viewsets.ViewSet):

    permission_classes: tuple = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs) -> Response:
        request.user.auth_token.delete()
        django_logout(request)
        return Response(
            {"detail": "Successfully logged out."}, status=status.HTTP_200_OK
        )
