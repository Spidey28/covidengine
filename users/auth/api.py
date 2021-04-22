from django.contrib.auth import logout
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from base import response, viewsets

from . import utils
from .serializers import AuthUserSerializer, LoginSerializer


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = LoginSerializer

    @action(
        methods=["POST"],
        detail=False,
    )
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = utils.get_and_authenticate_user(**serializer.validated_data)
        return response.Ok(AuthUserSerializer(instance=user).data)

    @action(
        methods=["POST"],
        detail=False,
        permission_classes=[
            IsAuthenticated,
        ],
    )
    def logout(self, request):
        utils.delete_token(request.user)
        logout(request)
        return response.Ok({"success": "Successfully logged out"})
