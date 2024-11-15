from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse

from catalogue.models import Species

def description(request, id):
    if id > Species.objects.count():
        return HttpResponse("URL incorrecte : il n'existe pas d'ID d'espèce n°"+str(id)+".")
                            
    species = get_object_or_404(Species, id=id)
    #return HttpResponse(species.name)
    return render(request, 'description/description.html', {"id":id})

def error(request, text):
    return HttpResponse("URL incorrecte : entrer un nombre entre 1 et "+str(Species.objects.count()))