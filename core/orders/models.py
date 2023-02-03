from django.db import models
from customers.models import Customer
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cost = models.FloatField()
    # todo: count cost auto by func

    def __str__(self):
        return f'user_id:{self.user.pk}, cost:{self.cost}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField()

    def get_computed(self):
        return self.product.cost * self.number

    def save(self, *args, **kwargs):
        self.cost = self.get_computed()
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'order_id:{self.order.pk}, product:{self.product.name}'
