from rest_framework import viewsets, status
from rest_framework.response import Response

from app.endpoints.user_profile.utils import create_user


class SignUpViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs) -> Response:
        data = request.data
        create_user(data=data)
        return Response({"message": "Account created"}, status=status.HTTP_201_CREATED)
