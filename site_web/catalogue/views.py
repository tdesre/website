from django.shortcuts import render
from .models import Species

def catalogue_feuilles(request):
    feuilles = Species.objects.exclude(name_leaf="").all()
    context = {'species_list': feuilles, 'type': 'Feuilles'}
    return render(request, 'catalogue/catalogue.html', context)

def catalogue_fruits(request):
    fruits = Species.objects.exclude(name_fruit="").all()
    context = {'species_list': fruits, 'type': 'Fruits'}
    return render(request, 'catalogue/catalogue.html', context)
