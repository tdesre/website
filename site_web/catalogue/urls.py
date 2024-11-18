from django.urls import path
from . import views

urlpatterns = [
    path('feuilles/', views.catalogue_feuilles, name='catalogue_feuilles'),
]