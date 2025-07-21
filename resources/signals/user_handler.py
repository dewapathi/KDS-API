from django.dispatch import receiver
from resources.signals import user_create
from resources.services import create_user_with_address

@receiver(user_create)
def on_user_create(sender, **kwargs):
    create_user_with_address(**kwargs)