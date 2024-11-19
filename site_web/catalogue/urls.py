from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalogue_home, name='catalogue_home'),
    path('feuilles/', views.catalogue_feuilles, name='catalogue_feuilles'),
    path('fruits/', views.catalogue_fruits, name='catalogue_fruits'),
    path('feuilles/<str:species_name>/', views.species_detail, name='species_detail'),  # Ajout de cette ligne
    path('search/<str:text>/', views.species_search_view, name='species_search'),
]
