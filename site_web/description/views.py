from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.forms.models import model_to_dict
from catalogue.models import Species
import os
from django.views.decorators.csrf import csrf_exempt


def description(request, id):

    # Vérifier que l'URL est bonne
    if id == 0 :
        return redirect('/description/'+str(Species.objects.count()))
    if id > Species.objects.count():
        return redirect('/description/1')
    
    # Créé la liste de chemins d'accès aux photos de l'espèce
    species = get_object_or_404(Species, id=id)
    images_path = []
    for filename in os.listdir(species.folder_gallery):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            images_path.append(species.folder_gallery+str("/")+filename)

    # Trouve la description
    try:
        with open(species.description, 'r', encoding='utf-8') as file:
            species.description = file.read()
    except FileNotFoundError:
        species.description = "Fichier non trouvé."
    
    # Choisis la couleur de l'icône coeur
    if request.user.is_authenticated and (request.user.username in species.user_name.split(",")):
        favorite = True
    else:
        favorite = False

    context= {**model_to_dict(species), 'images_path': images_path, 'is_red': favorite}
    return render(request, 'description/description.html', context)

@csrf_exempt
def update_favorite(request, id):
    print("1")
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        # Vérifier que l'URL est bonne
        if id == 0 :
            return redirect('/description/'+str(Species.objects.count()))
        if id > Species.objects.count():
            return redirect('/description/1')
    
        species = get_object_or_404(Species, id=id)

        if request.user.is_authenticated and (request.user.username in species.user_name.split(",")):
            print('2', species.user_name)
            species.user_name = species.user_name.replace(request.user.username + ",", "")

            species.save()
            print(species.user_name)
        elif request.user.is_authenticated and (request.user.username not in species.user_name.split(",")):
            print('3')
            species.user_name = species.user_name + request.user.username + ","
            species.save()
        else:
            print('pas connecté')
        
        return redirect('/description/'+str(id))

def error(request, text):
    return HttpResponse("URL incorrecte : entrer un nombre entre 1 et "+str(Species.objects.count()))