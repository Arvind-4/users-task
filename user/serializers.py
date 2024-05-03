from rest_framework import serializers
from user.models import User, Manager
from user.utils import validate_pan_num, validate_indian_phone_number


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


class UserCreateSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    mob_num = serializers.CharField()
    pan_num = serializers.CharField()
    manager_id = serializers.UUIDField(required=False)

    def validate_pan_num(self, pan_num):
        val = validate_pan_num(pan_num)
        if not val:
            raise serializers.ValidationError("Invalid PAN number.")
        return pan_num

    def validate_mob_num(self, mob_num):
        val = validate_indian_phone_number(mob_num)
        if not val:
            raise serializers.ValidationError("Invalid mobile number.")
        return mob_num

    def validate(self, data):
        manager_id = data.get("manager_id")
        if manager_id is None:
            data["manager_id"] = None
            return data
        try:
            Manager.objects.get(manager_id=manager_id)
            data["manager_id"] = manager_id
        except Manager.DoesNotExist:
            data["manager_id"] = None
            raise serializers.ValidationError("Invalid manager ID.")
        return data


def validate_mob_num(self, mob_num):
    val = validate_indian_phone_number(mob_num)
    if not val:
        raise serializers.ValidationError("Invalid mobile number.")
    return mob_num


class UserUpdateSerializer(serializers.Serializer):
    user_id = serializers.UUIDField(required=True)
    full_name = serializers.CharField(max_length=255, required=False)
    mob_num = serializers.CharField(required=False)
    pan_num = serializers.CharField(required=False)
    manager_id = serializers.UUIDField(required=False)

    def validate_pan_num(self, pan_num):
        val = validate_pan_num(pan_num)
        if not val:
            raise serializers.ValidationError("Invalid PAN number.")
        return pan_num

    def validate_mob_num(self, mob_num):
        val = validate_indian_phone_number(mob_num)
        if not val:
            raise serializers.ValidationError("Invalid mobile number.")
        return mob_num

    def validate(self, data):
        manager_id = data.get("manager_id")
        if manager_id is None:
            data["manager_id"] = None
            return data
        try:
            Manager.objects.get(manager_id=manager_id)
            data["manager_id"] = manager_id
        except Manager.DoesNotExist:
            data["manager_id"] = None
            raise serializers.ValidationError("Invalid manager ID.")
        return data
