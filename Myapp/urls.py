from django.urls import path
from . import views

urlpatterns = [
       path('', views.home, name='home'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/create/', views.car_create, name='car_create'),
    path('cars/<int:pk>/edit/', views.car_update, name='car_update'),
    path('cars/<int:pk>/delete/', views.car_delete, name='car_delete'),
    path('services/', views.service_list, name='service_list'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/edit/', views.service_update, name='service_update'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),
]