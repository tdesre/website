from django.shortcuts import render
from .models import Species

def catalogue(request):
    # Récupération de toutes les espèces
    species_list = Species.objects.all()
    context = {'species_list': species_list}
    return render(request, 'catalogue/catalogue.html', context)


def list_items(request, category):
    context = {'category': category}
    return render(request, 'catalogue/list.html', context)
