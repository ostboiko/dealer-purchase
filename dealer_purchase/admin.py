from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ModelCar, Manufacturer, Dealer


@admin.register(Dealer)
class DealerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("license_number",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "license_number",
                    )
                },
            ),
        )
    )


@admin.register(ModelCar)
class ModelCarAdmin(admin.ModelAdmin):
    search_fields = ("model__car",)
    list_filter = ("manufacturer",)


admin.site.register(Manufacturer)
