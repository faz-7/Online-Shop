from .models import User
from django.core.exceptions import ValidationError
from django import forms


class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(label='full name')
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('email already exists')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError('Phone number already exists')
        return phone


class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
