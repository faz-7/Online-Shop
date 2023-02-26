from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User


class UserRegisterView(View):
    form = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['email'], cd['password'], phone_number=cd['phone_number'],
                                     full_name=cd['full_name'])

            messages.success(request, 'registered successfully', 'success')
            return redirect('products:landing')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully', 'success')
        return redirect('products:landing')


class UserLoginView(View):
    form = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, f'{user.full_name} Logged in successfully', 'info')
                return redirect('products:landing')
            messages.error(request, 'email or password is wrong', 'warning')
        return render(request, self.template_name, {'form': form})


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'accounts/profile.html')