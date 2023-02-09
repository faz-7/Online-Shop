from django.core.validators import RegexValidator
from django.db import models
from ckeditor.fields import RichTextField


class Discount(models.Model):  # todo: write validation for amount not greater than 100% or amount
    amount = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    TYPES = (
        ('P', 'Percent'),
        ('C', 'Cash'),
    )
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return f'type:{self.type}, amount:{self.amount}'


class Category(models.Model):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'name:{self.name}'


class Product(models.Model):  # todo: write func to calculate cost by considering discount
    categories = models.ManyToManyField(Category, related_name='product_category')
    discounts = models.ManyToManyField(Discount, related_name='product_discount', blank=True)
    name = models.CharField(max_length=20)
    image = models.ImageField()
    brand = models.CharField(max_length=20, blank=True, default='empty')
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'name:{self.name}, cost:{self.price}'
