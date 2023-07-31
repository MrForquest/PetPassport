import rest_framework.serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(rest_framework.serializers.ModelSerializer):
    avatar = rest_framework.serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "avatar",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True},
            "username": {"required": True},
        }

    def get_avatar(self, obj):
        avatar = {
            "avatar_full": obj.avatar.image.url,
            "avatar_tmb": obj.avatar.image_tmb_url(),
        }
        return avatar

    def create(self, validated_data):
        user = User(
            email=validated_data["email"], username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
