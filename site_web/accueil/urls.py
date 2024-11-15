from django.urls import path
from . import views  


app_name = 'accueil'

urlpatterns = [
    path('', views.accueil, name='accueil'),
]