from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Species

'''
def index(request):
    # Chargement du template avec le chemin relatif approprié
    template = loader.get_template('catalogue/catalogue.html')
    
    # Rendu du template avec le contexte de la requête
    return HttpResponse(template.render(request=request))
'''

def catalogue_feuilles(request):
    feuilles = Species.objects.exclude(name_leaf="").all()
    context = {'species_list': feuilles, 'type': 'Feuilles'}
    return render(request, 'catalogue/catalogue.html', context)