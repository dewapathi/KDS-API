from django.db import transaction
from core.models import User, Address


def create_user_with_address(user_data, address_data, password, **kwargs):
    with transaction.atomic():
        user_instance = User(**user_data)
        user_instance.set_password(password)
        user_instance.save()

        Address.objects.create(user=user_instance, **address_data)

        return user_instance
