from django.contrib import admin
from .models import User, Address


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name", "phone_number")
    list_filter = ("last_login",)
    search_fields = ("email", "full_name")
    ordering = ("full_name",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("province", "city")
    list_filter = ("province",)
    search_fields = ("city",)

# supervisor -> supervisor@gmail.com , secret
# manager -> manager@gmail.com , secret
# operator -> operator@gmail.com , secret
