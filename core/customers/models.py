from django.core.validators import RegexValidator
from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=50, blank=True, default='empty')
    lastname = models.CharField(max_length=50, blank=True, default='empty')
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], null=True, blank=True,
                                    help_text='without leading zero')
    email = models.EmailField(blank=True, default='empty', help_text='example@example.com')

    def __str__(self):
        return f'id:{self.pk}, username:{self.username}'


class Address(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    avenue = models.CharField(max_length=50)
    plate = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])

    def __str__(self):
        return f'user_id:{self.user.id}, province:{self.province}'
