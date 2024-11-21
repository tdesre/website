from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accueil'),  # url pour acceder à l'accueil
    path('login/', views.Connect, name='login'), # url pour le formulaire de connexion
    path('register/', views.Register, name='register'), #url pour le formulaire de création d'un nouveau profil
]
