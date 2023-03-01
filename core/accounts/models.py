from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from PIL import Image


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(validators=[RegexValidator(r'^\+?1?\d{9,10}$')], max_length=11, unique=True)
    image = models.ImageField(upload_to='profile_pic', default='user_default_avatar.png')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    avenue = models.CharField(max_length=50)
    plate = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])

    def __str__(self):
        return f'user_id:{self.user.id}, province:{self.province}'
