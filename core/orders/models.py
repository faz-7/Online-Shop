from django.db import models
from accounts.models import User
from products.models import Product


class Order(models.Model):  # todo: write method return cost of order using related_name add date
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('paid',)

    def __str__(self):
        return f'user_id:{self.user.pk}'

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):  # todo: write method to calculate each orderItem price
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'order_id:{self.order.pk}, product:{self.product.name}'

    def get_cost(self):
        return self.product.price * self.quantity
