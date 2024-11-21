from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.forms.models import model_to_dict
from catalogue.models import Species
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path  
from django.conf import settings
from unicodedata import normalize
import os

def normalize_name(input_str):
    """Supprime les accents et remplace les espaces par des underscores."""
    # Supprimer les accents
    no_accents = ''.join(c for c in normalize('NFD', input_str) if c.isascii())
    # Remplacer les espaces par des underscores
    return no_accents.replace(' ', '_')

def description(request, id):
    if id == 0:
        return redirect('/description/' + str(Species.objects.count()))
    if id > Species.objects.count():
        return redirect('/description/1')

    # Récupérer l'espèce
    species = get_object_or_404(Species, id=id)

    # Normaliser le nom pour éviter les problèmes d'accents et d'espaces
    normalized_name = normalize_name(species.name.lower())

    # Chemin vers la galerie d'images
    gallery_folder = Path(settings.BASE_DIR) / "catalogue" / "gallery" / f"{normalized_name}_gallery"
    images_path = []

    # Vérifie si le dossier existe et récupère les fichiers images
    if gallery_folder.exists() and gallery_folder.is_dir():
        for file in gallery_folder.iterdir():
            if file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif']:
                images_path.append(f"/catalogue/gallery/{normalized_name}_gallery/{file.name}")

    # Chemin vers le fichier de description
    description_folder = Path(settings.BASE_DIR) / "description" / "descriptions"
    description_file = description_folder / f"{normalized_name}.txt"

    try:
        if description_file.exists() and description_file.is_file():
            with description_file.open('r', encoding='utf-8') as file:
                species.description = file.read()
        else:
            # Si le fichier est introuvable
            species.description = f"Aucune description disponible pour {species.name}."
    except Exception as e:
        # Gestion des erreurs de lecture
        species.description = f"Erreur lors de la lecture de la description : {e}"

    # Préparer le contexte pour le template

    if request.user.is_authenticated and (request.user.username in species.user_name.split(",")):
        favorite = True
    else:
        favorite = False

    context = {
        **model_to_dict(species),
        'images_path': images_path,
        'is_red': favorite,
    }
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
    return HttpResponse("URL incorrecte : entrer un nombre entre 1 et " + str(Species.objects.count()))
