from django.urls import path
from . import views

name_space = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('updateProfile/', views.UserUpdateProfileView.as_view(), name='user_update_profile'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('address/', views.UserAddressView.as_view(), name='user_address'),
    path('add-address/', views.AddressCreationView.as_view(), name='user_add_address'),
    path('edit-address/<int:address_id>/', views.EditAddressView.as_view(), name='user_edit_address'),
    path('remove-address/<int:address_id>/', views.AddressRemoveView.as_view(), name='user_remove_address'),
]
