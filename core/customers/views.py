from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerLoginForm, CustomerRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer


class CustomerRegisterView(View):
    form = CustomerRegistrationForm
    template_name = 'customers/register.html'

    def get(self, request):
        form = self.form
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Customer.objects.create_user(cd['email'], cd['full_name'],
                                         cd['phone_number'], cd['password'])
            messages.success(request, 'registered successfully', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})


class CustomerLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully', 'success')
        return redirect('home:home')


class CustomerLoginView(View):
    form = CustomerLoginForm
    template_name = 'customers/login.html'

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
                messages.success(request, 'Logged in successfully', 'info')
                return redirect('home:home')
            messages.error(request, 'phone or password is wrong', 'warning')
        return render(request, self.template_name, {'form': form})
