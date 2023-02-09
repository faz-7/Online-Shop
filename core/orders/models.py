from django.db import models
from customers.models import Customer
from products.models import Product


class Order(models.Model):  # todo: write method return cost of order using related_name
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('paid',)

    def __str__(self):
        return f'user_id:{self.user.pk}'


class OrderItem(models.Model):  # todo: write method to calculate each orderItem price
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'order_id:{self.order.pk}, product:{self.product.name}'
