from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accueil'),  # Page d'accueil
    path('login/', views.Connect, name='login')
]
