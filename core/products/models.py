from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class Category(models.Model):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('products:category_filter', args=[self.id, ])

    def __str__(self):
        return f'name:{self.name}'


class Product(models.Model):  # todo: write func to calculate cost by considering discount
    categories = models.ManyToManyField(Category, related_name='product_category')
    name = models.CharField(max_length=20)
    image = models.ImageField()
    brand = models.CharField(max_length=20, blank=True, default='empty')
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, ])

    def __str__(self):
        return f'name:{self.name}, cost:{self.price}'


class Discount(models.Model):  # todo: write validation for amount not greater than 100% or amount
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    amount = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    TYPES = (
        ('P', 'Percent'),
        ('C', 'Cash'),
    )
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return f'type:{self.type}, amount:{self.amount}'

# link to calculate price by considering discount :
# https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
