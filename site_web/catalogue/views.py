from django.shortcuts import render
from django.db.models import Q
from .models import Species
from django.http import HttpResponse
from django.template import loader

def catalogue_feuilles(request):
    feuilles = Species.objects.exclude(file_leaf="")
    images = [{'type': 'Feuilles', 'path': feuille.file_leaf, 'id': feuille.id, 'portfolio_id':'portfolioModal'+str(feuille.id)} for feuille in feuilles]
    return render(request, 'catalogue/catalogue_feuilles.html', {'images' : images})

def catalogue_fruits(request):
    fruits = Species.objects.exclude(file_leaf="")
    images = [{'type': 'Fruits', 'path': fruit.file_fruit, 'id': fruit.id, 'portfolio_id':'portfolioModal'+str(fruit.id)} for fruit in fruits]
    return render(request, 'catalogue/catalogue_fruits.html', {'images' : images})

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
