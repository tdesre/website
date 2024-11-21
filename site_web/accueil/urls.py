from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accueil'),  
    path('login/', views.Connect, name='login'),
    path('register/', views.Register, name='register'),
]
