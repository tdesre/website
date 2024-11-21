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

# Fonction pour formater les species.name et retomber sur
# les fichier de leaf_photos, fruit_photos, et des descriptions
def normalize_name(input_str):
    """Supprime les accents et remplace les espaces par des underscores."""
    # Supprimer les accents
    no_accents = ''.join(c for c in normalize('NFD', input_str) if c.isascii())
    # Remplacer les espaces par des underscores
    return no_accents.replace(' ', '_')

def description(request, id):
    # si id = 0 n'existe pas, l'utilisateur est redirigé
    # sur la page du la dernière espèce (par défaut)
    if id == 0:
        return redirect('/description/' + str(Species.objects.count()))
    # si id plus grand que le nombre d'espèce n'existe pas
    # on redirige l'utilisateur sur la page de la première
    # espèce
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
        # Vérifie si le fichier de description existe et s'il s'agit bien d'un fichier
        if description_file.exists() and description_file.is_file():
            # Ouvre le fichier en mode lecture ('r') avec l'encodage UTF-8
            with description_file.open('r', encoding='utf-8') as file:
                # Lit le contenu du fichier et le stocke dans species.description
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
    
        species = get_object_or_404(Species, id=id)  # Récupère l'objet espèce

        if request.user.is_authenticated and (request.user.username in species.user_name.split(",")):
            species.user_name = species.user_name.replace(request.user.username + ",", "") # Le profil n'aime plus l'espèce
            species.save()
        elif request.user.is_authenticated and (request.user.username not in species.user_name.split(",")):
            species.user_name = species.user_name + request.user.username + "," # Le profil aime l'espèce
            species.save()
        else:
            print('pas connecté')
        
        return redirect('/description/'+str(id)) # Si jamais il y a une erreur

def error(request, text):
    return HttpResponse("URL incorrecte : entrer un nombre entre 1 et " + str(Species.objects.count()))
