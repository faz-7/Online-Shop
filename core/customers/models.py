from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.models import User


class Customer(User):  # todo: fix staff as always false
    full_name = models.CharField(max_length=100)
    # todo: validate phone number
    phone_number = models.CharField(max_length=11, unique=True)
    image = models.ImageField(upload_to='customers/')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


class Address(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    avenue = models.CharField(max_length=50)
    plate = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])

    def __str__(self):
        return f'user_id:{self.user.id}, province:{self.province}'
