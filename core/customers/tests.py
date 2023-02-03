from django.test import TestCase
from .models import Customer, Address


class CustomerModelsTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(username='user1', password='123')
        self.address = Address.objects.create(user_id=self.customer, province='Isfahan', city='Isfahan',
                                              avenue='azadi',
                                              plate=13)

    def test_customer(self):  # python manage.py test --keepdb
        self.assertEqual(str(self.customer), self.customer.username)

    def test_address(self):
        self.assertEqual(self.customer, self.address.user)
