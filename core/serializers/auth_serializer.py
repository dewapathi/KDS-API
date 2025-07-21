from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import User, Address
from resources.signals import user_create


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "full_name",
            "phone",
            "address_type",
            "is_default",
            "line1",
            "line2",
            "city",
            "state",
            "postal_code",
            "country",
        ]


class UserSignUpSerializer(serializers.ModelSerializer):
    address = AddressSerializer(write_only=True)
    password = serializers.CharField(write_only=True, min_length=4)

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone",
            "password",
            "user_type",
            "address",
        ]

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        password = validated_data.pop("password")

        user_create.send_robust(
            sender=self.__class__,
            user_data=validated_data,
            address_data=address_data,
            password=password,
        )

        return validated_data


class UserSignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials")

        if not user.is_active:
            raise serializers.ValidationError("Account is not active")

        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "user_type": user.user_type,
            },
        }
