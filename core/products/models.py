from django.core.exceptions import ValidationError
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


class Product(models.Model):
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
        return self.name

    def get_final_price(self):
        discount = Discount.objects.get(product=self)
        if discount.type == 'P':
            return self.price * (1 - discount.amount / 100)
        return self.price - discount.amount


class Discount(models.Model):  # todo: write validation for amount not greater than 100% or amount
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    TYPES = (
        ('P', 'Percent'),
        ('C', 'Cash'),
    )
    type = models.CharField(max_length=1, choices=TYPES)
    amount = models.IntegerField()

    def __str__(self):
        return f'type:{self.type}, amount:{self.amount}'

    # def clean_amount(self, exclude=None): # todo: handle this in DiscountCreationForm
    #     super().clean_fields(exclude=exclude)
    #     if (self.type == 'P' and self.amount >= 100) or (self.type == 'C' and self.amount >= self.product.price):
    #         raise ValidationError('Invalid amount for discount!')
    #     return self.amount

# link to calculate price by considering discount :
# https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
