from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogue, name='catalogue'),  # Page principale du catalogue
    path('<str:category>/', views.list_items, name='list_items'),  # Liste des feuilles ou fruits
]
