from django.urls import path
from . import views  


app_name = 'description'

urlpatterns = [
    path('', views.description, name='descritption'),
]