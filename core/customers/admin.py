from django.contrib import admin
from .models import Customer, Address


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name", "phone_number")
    list_filter = ("last_login",)
    search_fields = ("email", "full_name")
    ordering = ("full_name",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("province", "city")
    list_filter = ("province",)
    search_fields = ("city",)
