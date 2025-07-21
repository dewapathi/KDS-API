from rest_framework import serializers

from core.models import User, Address


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

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        Address.objects.create(user=user, **address_data)
        
        return user
