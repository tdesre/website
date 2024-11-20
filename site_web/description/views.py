from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.forms.models import model_to_dict
from catalogue.models import Species
from pathlib import Path  # Utilisation de pathlib pour la gestion des chemins

from pathlib import Path
from django.conf import settings

def description(request, id):
    if id == 0:
        return redirect('/description/' + str(Species.objects.count()))
    if id > Species.objects.count():
        return redirect('/description/1')

    # Récupérer l'espèce
    species = get_object_or_404(Species, id=id)

    # Chemin vers la galerie d'images
    gallery_folder = Path(settings.BASE_DIR) / "catalogue" / "gallery" / f"{species.name.lower()}_gallery"
    images_path = []

    # Vérifie si le dossier existe et récupère les fichiers images
    if gallery_folder.exists() and gallery_folder.is_dir():
        for file in gallery_folder.iterdir():
            if file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif']:
                images_path.append(f"/catalogue/gallery/{species.name.lower()}_gallery/{file.name}")

    # Chemin vers le fichier de description
    description_folder = Path(settings.BASE_DIR) / "description" / "descriptions"
    description_file = description_folder / f"{species.name.lower()}.txt"
    if description_file.exists() and description_file.is_file():
        try:
            with description_file.open('r', encoding='utf-8') as file:
                species.description = file.read()
        except Exception as e:
            species.description = f"Erreur lors de la lecture de la description : {e}"
    else:
        species.description = "Description introuvable."

    # Logs pour diagnostic
    print("Chemin galerie :", gallery_folder)
    print("Images trouvées :", images_path)
    print("Chemin description :", description_file)
    print("Description :", species.description)

    # Préparer le contexte pour le template
    context = {
        **model_to_dict(species),
        'images_path': images_path,
        'is_red': request.user.is_authenticated,
    }
    return render(request, 'description/description.html', context)

def error(request, text):
    return HttpResponse("URL incorrecte : entrer un nombre entre 1 et " + str(Species.objects.count()))
