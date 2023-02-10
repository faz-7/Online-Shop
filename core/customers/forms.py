from .models import Customer
from django.core.exceptions import ValidationError
from django import forms


class CustomerRegistrationForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(label='full name')
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = Customer.objects.filter(email=email).exists()
        if user:
            raise ValidationError('email already exists')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone_number']
        user = Customer.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError('Phone number already exists')
        return phone


class CustomerLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
