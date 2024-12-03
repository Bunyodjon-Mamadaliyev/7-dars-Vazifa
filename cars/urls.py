from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.cars_list, name='cars_list'),
    path('cars/create/', views.cars_form, name='new')
]