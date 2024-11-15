from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static

from . import views
from . import models

urlpatterns = [
    path('<int:id>/', views.description, name="description"), # URL de chaque espèce : /description/[id espèce]
    path('<str:text>/', views.error, name="error") # si l'URL /description/[texte] correspond à rien
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)