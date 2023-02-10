from django.contrib import admin
from .models import Manager, Supervisor, Operator


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ("email", "password")

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True

    def has_view_or_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ("email", "password")

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True

    def has_view_or_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ("email", "password")

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True

    def has_view_or_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
