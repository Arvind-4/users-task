from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "user_id",
            "manager_id",
            "full_name",
            "mob_num",
            "pan_num",
            "created_at",
            "updated_at",
            "is_active",
        )
        read_only_fields = ("user_id", "created_at")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["manager_id"] = str(data["manager_id"]) if data["manager_id"] else None
        data["user_id"] = str(data["user_id"])
        return data
