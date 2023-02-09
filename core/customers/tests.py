from django.test import TestCase

from .models import Customer, Address


class ProductModelsTest(TestCase):
    def setUp(self):
        self.user = Customer.objects.create(email='temp@gmail.com', password='123')
        self.address = Address.objects.create(user=self.user, province='isfahan', city='isfahan', avenue='azad',
                                              plate=12)

    def test_customer(self):
        self.assertEqual(self.address.user.email, self.user.email)
