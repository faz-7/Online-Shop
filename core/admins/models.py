from django.db import models
from accounts.models import User


class Manager(User):
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=True)


class Supervisor(User):
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_supervisor = models.BooleanField(default=True)


class Operator(User):
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_operator = models.BooleanField(default=True)

# manager -> manager@gmail.com - 'secret'
# supervisor -> supervisor@gmail.com - 'secret'
# operator -> operator@gmail.com - 'secret'
