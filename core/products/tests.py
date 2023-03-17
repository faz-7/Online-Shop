from django.test import TestCase
from .models import Product, Discount, Category


class ProductModelsTest(TestCase):
    def setUp(self):
        self.main_category = Category.objects.create(name='hygienic')
        self.sub_category = Category.objects.create(name='cosmetic', parent=self.main_category)
        self.product = Product.objects.create(name='laptop', image='static/img/macbook.jpg', description='empty',
                                              price=42, available=True)
        self.discount = Discount.objects.create(product=self.product, amount='20', type='P')
        self.product.categories.add(self.sub_category)

    def test_category(self):
        self.assertEqual(self.sub_category.parent, self.main_category)

    def test_discount(self):
        self.assertEqual(self.discount.amount, self.product.products.get(pk=self.discount.pk))

    def test_product(self):
        self.assertEqual(self.product.categories.get(pk=self.sub_category.pk).parent, self.main_category)
