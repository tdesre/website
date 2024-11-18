from django.urls import path
from . import views

urlpatterns = [
    # URL avec un paramètre dynamique 'text'
    path('search/<str:text>/', views.species_search_view, name='species_search'),
]
