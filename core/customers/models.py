from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=50, blank=True, default='empty')
    lastname = models.CharField(max_length=50, blank=True, default='empty')
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], null=True, blank=True,
                                    help_text='without leading zero')
    email = models.EmailField(blank=True, default='empty', help_text='example@example.com')

    # todo: write str and admin.register


class Address(models.Model):
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    avenue = models.CharField(max_length=50)
    plate = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
