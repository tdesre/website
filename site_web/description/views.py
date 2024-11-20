from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.forms.models import model_to_dict
from catalogue.models import Species
import os

def description(request, id):
    if id == 0 :
        return redirect('/description/'+str(Species.objects.count()))
    if id > Species.objects.count():
        return redirect('/description/1')
    
    species = get_object_or_404(Species, id=id)
    images_path = []
    for filename in os.listdir(species.folder_gallery):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            images_path.append(species.folder_gallery+str("/")+filename)

    try:
        with open(species.description, 'r', encoding='utf-8') as file:
            species.description = file.read()
    except FileNotFoundError:
        species.description = "Fichier non trouvé."

    context= {**model_to_dict(species), 'images_path': images_path, 'is_red': request.user.is_authenticated}
    return render(request, 'description/description.html', context)

def error(request, text):
    return HttpResponse("URL incorrecte : entrer un nombre entre 1 et "+str(Species.objects.count()))