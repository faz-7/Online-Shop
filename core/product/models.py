from django.core.validators import RegexValidator
from django.db import models


class Discount(models.Model):
    amount = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    TYPES = (
        ('P', 'Percent'),
        ('C', 'Cash'),
    )
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return f'type:{self.type}, amount:{self.amount}'


class Category(models.Model):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)

    # categories= models.ManyToManyField('Product', related_name="category_id")
    # if both needs access the interface table

    def __str__(self):
        return f'name:{self.name}'


class Product(models.Model):
    categories = models.ManyToManyField(Category)
    discounts = models.ManyToManyField(Discount, blank=True)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20, blank=True, default='empty')
    STATUS = (
        ('E', 'Exist'),
        ('F', 'Finish'),
    )
    status = models.CharField(max_length=1, choices=STATUS)
    information = models.TextField(blank=True, default='empty')
    cost = models.FloatField()
    # todo: write func to calculate cost by considering discount
    # todo: write method to add parent of category to m2m interface table

    def __str__(self):
        return f'name:{self.name}, cost:{self.cost}'
