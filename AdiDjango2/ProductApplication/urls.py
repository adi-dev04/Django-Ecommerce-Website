from django.urls import path
from . import  views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('login/', views.login, name='login'),
    path('insert/', views.insert, name='insert'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('prodetails/<int:pk>/', views.ProductDetailView.as_view(), name='prodetails'),
    path('custdetails/<int:pk>/',views.custdetails, name='custdetails'),
    path('order/<int:pk>/',views.OrderDetailView.as_view(),name='order'),
]