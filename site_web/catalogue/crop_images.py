#ATTENTION, ÇA MODIFIE LES IMAGES SI ON L'APPELLE

import os
from PIL import Image

# Fonction pour rogner une image selon un ratio de hauteur/largeur
def crop_image(image_path, ratio):
    with Image.open(image_path) as img:
        img_width, img_height = img.size
        
        # Calcul des nouvelles dimensions de rognage en fonction du ratio
        new_width = img_width
        new_height = int(new_width * ratio)
        
        if new_height > img_height:
            # Si la hauteur calculée est plus grande que l'image, ajuster la largeur
            new_height = img_height
            new_width = int(new_height / ratio)

        # Calcul du centre de l'image
        left = (img_width - new_width) / 2
        top = (img_height - new_height) / 2
        right = (img_width + new_width) / 2
        bottom = (img_height + new_height) / 2
        
        # Rogner l'image
        img_cropped = img.crop((left, top, right, bottom))
        
        # Sauvegarder l'image rognée en remplaçant l'original
        img_cropped.save(image_path)

# Fonction pour parcourir un dossier et rogner toutes les images
def crop_images_in_directory(directory, ratio):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                image_path = os.path.join(root, file)
                
                try:
                    crop_image(image_path, ratio)
                    print(f"Image rognée et remplacée : {image_path}")
                except Exception as e:
                    print(f"Erreur avec {image_path}: {e}")

# Paramètres
directory = "C:\\Users\\theop\\Desktop\\coding-weeks-site-web\\site_web\\catalogue\\gallery"  # Remplacez par le chemin du dossier
ratio = 0.625  # ratio hauteur/largeur 

# Lancer le script
crop_images_in_directory(directory, ratio)