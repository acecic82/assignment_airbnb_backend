from rest_framework.serializers import ModelSerializer

from users.models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
            "gender",
            "language",
            "currency",
        )
