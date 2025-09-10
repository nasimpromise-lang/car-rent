from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'fuel_type', 'price_per_week', 'price_per_month', 'photo')
    list_filter = ('fuel_type',)
    search_fields = ('name', 'model')
    fields = ('name', 'model', 'fuel_type', 'price_per_week', 'price_per_month', 'photo')

    def save_model(self, request, obj, form, change):
        obj.full_clean()  # Trigger the clean() validation
        super().save_model(request, obj, form, change)