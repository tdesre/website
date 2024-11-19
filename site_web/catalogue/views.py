from django.shortcuts import render, redirect, get_object_or_404
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
    query = Q(keywords__icontains=keyword) | Q(name_leaf__icontains=keyword) | Q(name_fruit__icontains=keyword)
    results = Species.objects.filter(query)  # Renvoie des objets Species
    return results

def species_search_view(request, text):
    keyword = text
    results = search_species(keyword)
    print("Résultats trouvés :", results)  # Vérifiez les données retournées
    return render(request, 'catalogue/search_results.html', {'results': results, 'keyword': keyword})

def catalogue_home(request):
    species_list = Species.objects.annotate(average_score=Avg('ratings__score'))  # Ajoute la moyenne des notes
    return render(request, 'catalogue/catalogue_home.html', {'species_list': species_list})

def species_detail(request, species_name):
    species = get_object_or_404(Species, name=species_name)
    return redirect('/description/'+str(species.id))