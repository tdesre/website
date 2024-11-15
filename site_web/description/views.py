from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.forms.models import model_to_dict
from catalogue.models import Species

def description(request, id):
    if id > Species.objects.count() or id < 1 :
        return HttpResponse("URL incorrecte : il n'existe pas d'ID d'espèce n°"+str(id)+".")
    species = get_object_or_404(Species, id=id)
    return render(request, 'description/description.html', model_to_dict(species))

def error(request, text):
    return HttpResponse("URL incorrecte : entrer un nombre entre 1 et "+str(Species.objects.count()))