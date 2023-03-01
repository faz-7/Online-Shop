import os

from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm, UserRegistrationForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


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


class UserUpdateProfileView(LoginRequiredMixin, View):
    form = UserChangeForm
    template_name = 'accounts/update_profile.html'

    def get(self, request):
        form = self.form(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('accounts:user_profile')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('accounts:user_profile')
