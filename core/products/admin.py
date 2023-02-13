from django.contrib import admin
from .models import Product, Discount, Category


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("amount", "type")
    list_filter = ("amount",)
    ordering = ("amount",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_name")
    list_filter = ("name",)
    search_fields = ("name",)

    def parent_name(self, obj):
        if obj.parent:
            return obj.parent.name

    parent_name.short_description = 'parent'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "available")
    list_filter = ("name", "price")
    search_fields = ("name", "brand")
