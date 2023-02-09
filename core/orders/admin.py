from django.contrib import admin
from .models import OrderItem, Order


@admin.register(Order)  # todo: add total cost after write method for it
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user_email", "items", "paid")
    list_filter = ("paid",)
    ordering = ("paid",)

    def user_email(self, obj):
        return obj.user.email

    def items(self, obj):
        return obj.items.count()

    items.short_description = 'items'
    user_email.short_description = 'customer email'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order_id", "product_name", "quantity")

    def order_id(self, obj):
        return obj.order.pk

    def product_name(self, obj):
        return obj.product.name

    order_id.short_description = 'order id'
    product_name.short_description = 'product'
