import django.contrib.auth.models
import django.db.models
from django.contrib.auth.hashers import make_password

import core.models


class User(django.contrib.auth.models.AbstractUser):
    pass


class UserAvatar(core.models.AbstractImageModel):
    def avatar_directory_path(self, instance, filename):
        return f"avatars/avatar_user_{instance.user.id}"

    image = django.db.models.ImageField(
        upload_to=avatar_directory_path,
        verbose_name="image",
        default="default/no-image.jpg",
    )
    user = django.db.models.OneToOneField(
        User,
        django.db.models.CASCADE,
        related_name="avatar",
    )

    class Meta:
        verbose_name = "user avatar"
        verbose_name_plural = "user avatars"
