from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

import users.views

app_name = "users"
auth_token_patterns = [
    path("", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns = [
    path("users/", users.views.UserCreate.as_view(), name="user-create"),
    path(
        "users/<int:pk>/", users.views.UserDetail.as_view(), name="user-detail"
    ),
    path("auth/token/", include(auth_token_patterns)),
]
