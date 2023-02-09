from django.test import TestCase
from .models import Product, Discount, Category


class ProductModelsTest(TestCase):
    def setUp(self):
        self.main_category = Category.objects.create(name='hygienic')
        self.sub_category = Category.objects.create(name='cosmetic', parent=self.main_category)
        self.discount = Discount.objects.create(amount='20', type='P')
        self.product = Product.objects.create(name='desk', image='static/img/macbook.jpg', description='empty',
                                              price=42, available=True)
        self.product.categories.add(self.sub_category)
        self.product.discounts.add(self.discount)

    def test_category(self):
        self.assertEqual(self.sub_category.parent, self.main_category)

    def test_discount(self):
        self.assertEqual(self.discount.amount, self.product.discounts.get(pk=self.discount.pk).amount)

    def test_product(self):
        self.assertEqual(self.product.categories.get(pk=self.sub_category.pk).parent, self.main_category)
