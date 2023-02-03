from django.test import TestCase

from customers.models import Customer
from product.models import Category, Product
from .models import Order, OrderItem


class ProductModelsTest(TestCase):
    def setUp(self):
        # create product instance
        self.category = Category.objects.create(name='hygienic')
        self.product = Product.objects.create(name='desk', status='E', cost=42)
        self.product.categories.add(self.category)

        # create customer instance
        self.user = Customer.objects.create(username='user1', password='123')

        self.order = Order.objects.create(user=self.user, status='U')
        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, number=2)
        self.order_item2 = OrderItem.objects.create(order=self.order, product=self.product, number=1)

    def test_order_item(self):
        self.assertEqual(self.order_item.cost, (self.product.cost * self.order_item.number))

    def test_order(self):
        self.assertEqual(self.order.cost, self.order_item.cost)
