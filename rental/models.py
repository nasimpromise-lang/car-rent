from django.db import models
from django.core.exceptions import ValidationError

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50, choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric')])
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.model}"

    def clean(self):
        if not self.price_per_week and not self.price_per_month:
            raise ValidationError("At least one of Price per Week or Price per Month must be provided.")