from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator

from .models import User
from django.core.exceptions import ValidationError
from django import forms


class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(label='full name')
    phone_number = forms.CharField(max_length=11, validators=[RegexValidator(r'^\+?1?\d{9,10}$')])
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('email already exists')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone_number')
        user = User.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError('Phone number already exists')
        return phone

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password and password:
            raise ValidationError('confirm password does not match password')
        return confirm_password


class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserChangeForm(forms.ModelForm):
    full_name = forms.CharField(label='full name')
    phone_number = forms.CharField(max_length=11, validators=[RegexValidator(r'^\+?1?\d{9,10}$')])
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'image']
