from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import JBIDetails, UserDetails

# user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # kalo mau custom user model ganti disini
        fields = ("id", "username", "email", "is_staff")


# register serializers
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )
        return user


# login serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = "__all__"

    def create(self, validated_data):
        return UserDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.gender = validated_data.get("gender", instance.gender)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.user_photo = validated_data.get("user_photo", instance.user_photo)
        instance.save()
        return instance