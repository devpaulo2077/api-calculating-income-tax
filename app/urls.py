from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('calculate/<str:value>/', views.calculate, name='calculate_without_deductions'),
    path('calculate/<str:value>/<str:deductions>/', views.calculate, name='calculate_with_deductions'),
]
