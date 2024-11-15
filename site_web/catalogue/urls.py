from django.urls import path
from . import views

urlpatterns = [
    path('feuilles/', views.catalogue_feuilles, name='catalogue_feuilles'),
    path('fruits/', views.catalogue_fruits, name='catalogue_fruits'),
]
