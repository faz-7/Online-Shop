from django.db import models


# Create your models here.
class AdminModel(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    # todo: tree types of admin with 3 different accessibility
