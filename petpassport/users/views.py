import django.http
import rest_framework.exceptions
import rest_framework.generics
import rest_framework.status
import rest_framework.views
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
import rest_framework.response
from users.models import User, UserAvatar
from users.serializers import UserSerializer


class UserCreate(rest_framework.generics.CreateAPIView):
    swagger_tags = ["users"]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        try:
            user.avatar
        except User.avatar.RelatedObjectDoesNotExist:
            avatar = UserAvatar(user=user)
            avatar.save()


class UserDetail(rest_framework.generics.RetrieveAPIView):
    swagger_tags = ["users"]
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
