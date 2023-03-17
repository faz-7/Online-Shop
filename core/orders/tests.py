from django.test import TestCase

from customers.models import Customer
from products.models import Category, Product
from .models import Order, OrderItem


class ProductModelsTest(TestCase):
    def setUp(self):
        # create products instance
        self.category = Category.objects.create(name='hygienic')
        self.product = Product.objects.create(name='desk', image='static/img/macbook.jpg', description='empty',
                                              price=42, available=True)
        self.product.categories.add(self.category)

        # create customer instance
        self.user = Customer.objects.create(email='temp@gmail.com', password='123')

        self.order = Order.objects.create(user=self.user, paid=False)
        self.order_item1 = OrderItem.objects.create(order=self.order, product=self.product, quantity=2)
        self.order_item2 = OrderItem.objects.create(order=self.order, product=self.product, quantity=1)

    def test_order(self):
        self.assertEqual(self.order_item1, self.order.items.get(pk=self.order_item1.pk))
