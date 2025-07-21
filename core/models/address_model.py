from django.db import models
from core.models import User


class Address(models.Model):
    ADDESS_TYPES_CHOICES = [("billing", "Billing"), ("shipping", "Shipping")]

    user = models.ForeignKey(User, related_name="addresses", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address_type = models.CharField(
        max_length=20, choices=ADDESS_TYPES_CHOICES, default="shipping"
    )
    is_default = models.BooleanField(default=False)
    line1 = models.CharField("Address Line 1", max_length=255)
    line2 = models.CharField("Address Line 2", max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField("State/Province", max_length=100)
    postal_code = models.CharField("ZIP/Postal Code", max_length=20)
    country = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "addresses"
        ordering = ["-is_default", "-updated_at"]

    def __str__(self):
        return f"{self.address_type.capitalize()} | {self.city}, {self.country} for {self.user.email}"
