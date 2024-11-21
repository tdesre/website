from django.conf import settings
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('<int:id>/update_favorite/', views.update_favorite, name="change_favorite"), # Mettre ou enlever des favoris
    path('<int:id>/', views.description, name="description"), # URL de chaque espèce : /description/[id espèce]
    path('<str:text>/', views.error, name="error"), # si l'URL /description/[texte] correspond à rien
]