from django.shortcuts import render
from django.db.models import Q
from .models import Species
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

def catalogue_feuilles(request):
    feuilles = Species.objects.exclude(name_leaf="").all()
    context = {'species_list': feuilles, 'type': 'Feuilles'}
    return render(request, 'catalogue/catalogue.html', context)
'''
def search_species(keyword):
    # Utilisation de Q pour construire la requête de recherche
    query = Q(keywords__icontains=keyword) | Q(name_leaf__icontains=keyword) | Q(name_fruit__icontains=keyword)
    
    # Filtrer les résultats en fonction de la requête
    results = Species.objects.filter(query)
    
    # Retourner les résultats (par exemple, les noms des espèces trouvées)
    return results.values_list('name', flat=True)  # Renvoie une liste de noms d'espèces
'''
def search_species(keyword):
    query = Q(keywords__icontains=keyword) | Q(name_leaf__icontains=keyword) | Q(name_fruit__icontains=keyword)
    results = Species.objects.filter(query)  # Renvoie des objets Species
    return results

def species_search_view(request, text):
    keyword = text
    results = search_species(keyword)
    print("Résultats trouvés :", results)  # Vérifiez les données retournées
    return render(request, 'catalogue/search_results.html', {'results': results, 'keyword': keyword})


def catalogue_home(request):
    return render(request, 'catalogue/catalogue_home.html')

def species_detail(request, species_name):
    species = get_object_or_404(Species, name=species_name)
    return render(request, 'catalogue/species_detail.html', {'species': species})