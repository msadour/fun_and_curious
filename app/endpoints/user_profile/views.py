from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.endpoints.user_profile.serializers import ProfileSerializer


class ManageProfileViewSet(viewsets.ViewSet):
    permission_classes = [
        IsAuthenticated,
    ]

    def patch(self, request):
        current_user = request.user
        data = request.data
        ProfileSerializer().update(instance=current_user, validated_data=data)
        return Response(status=status.HTTP_200_OK)

    def list(self, request):
        pass

    def retrieve(self, request):
        pass

    def destroy(self, request):
        pass

