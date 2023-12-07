from rest_framework import serializers
from apps.engine.schemas.user import User, SystemRoleEnum
from apps.engine.schemas.activities import Activities
from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.system_role
            in [SystemRoleEnum.ADMIN.value, SystemRoleEnum.SUPER_ADMIN.value]
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class UserAllProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ["data"]

    def create(self, validated_data):
        user = Activities.objects.create(**validated_data)
        return user
