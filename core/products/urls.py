from django.urls import path
from . import views

name_space = 'products'
urlpatterns = [
    path('', views.LandingView.as_view(), name='landing'),
    path('category/<int:category_id>/', views.LandingView.as_view(), name='category_filter'),
    path('<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
]
