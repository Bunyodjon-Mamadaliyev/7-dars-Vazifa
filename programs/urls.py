from django.urls import path
from . import views


app_name = 'programs'

urlpatterns = [
    path('', views.programs_list, name='app'),
    path('prog/', views.programs_form, name='new'),
]