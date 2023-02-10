from django.urls import path
from . import views

app_name = 'customers'
urlpatterns = [
    path('register/', views.CustomerRegisterView.as_view(), name='user_register'),
    path('login/', views.CustomerLoginView.as_view(), name='user_login'),
    path('logout/', views.CustomerLogoutView.as_view(), name='user_logout'),
]
