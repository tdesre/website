from django.shortcuts import render
from django.db.models import Q
from .models import Species
from django.http import HttpResponse
from django.template import loader

def catalogue_feuilles(request):
    feuilles = Species.objects.exclude(name_leaf="").all()
    context = {'species_list': feuilles, 'type': 'Feuilles'}

def search_species(keyword):
    # Utilisation de Q pour construire la requête de recherche
    query = Q(keywords__icontains=keyword) | Q(name_leaf__icontains=keyword) | Q(name_fruit__icontains=keyword)
    
    # Filtrer les résultats en fonction de la requête
    results = Species.objects.filter(query)
    
    # Retourner les résultats (par exemple, les noms des espèces trouvées)
    return results.values_list('name', flat=True)  # Renvoie une liste de noms d'espèces


def species_search_view(request, text):
    keyword = text
    results = search_species(keyword)
    print ("abs")
    return render(request, 'catalogue/search_results.html', {'results': results, 'keyword': keyword})


def catalogue_home(request):
    return render(request, 'catalogue/catalogue_home.html')
