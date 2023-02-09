from django.db import models
from customers.models import Customer
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    STATUS = (
        ('P', 'Paid'),
        ('U', 'Unpaid'),
    )
    status = models.CharField(max_length=1, choices=STATUS)

    def update_cost(self, new_item_price):  # todo: make it better work!
        items = OrderItem.objects.filter(order_id__exact=self.pk)
        res = sum(item.get_computed() for item in items)
        self.cost = res + new_item_price
        self.save()

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
        self.order.update_cost(self.cost)
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'order_id:{self.order.pk}, product:{self.product.name}'
