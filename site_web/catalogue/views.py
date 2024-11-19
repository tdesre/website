from django.shortcuts import render, redirect
from django.db.models import Q, Avg
from .models import Species, Rating
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

def catalogue_feuilles(request):
    feuilles = Species.objects.exclude(file_leaf="")
    images = [{'type': 'Feuilles', 'path': feuille.file_leaf, 'id': feuille.id, 'portfolio_id':'portfolioModal'+str(feuille.id)} for feuille in feuilles]
    dico = {}
    for i in range(len(images)):
        dico[f'{i}'] = (images[i], feuilles[i])
    return render(request, 'catalogue/catalogue_feuilles.html', {'dico' : dico})
    

def catalogue_fruits(request):
    fruits = Species.objects.exclude(file_leaf="")
    images = [{'type': 'Fruits', 'path': fruit.file_fruit, 'id': fruit.id, 'portfolio_id':'portfolioModal'+str(fruit.id)} for fruit in fruits]
    return render(request, 'catalogue/catalogue_fruits.html', {'images' : images})

def search_species(keyword):
    query = Q(keywords__icontains=keyword) | Q(name_leaf__icontains=keyword) | Q(name_fruit__icontains=keyword)
    results = Species.objects.filter(query)  # Renvoie des objets Species
    return results

def species_search_view(request, text):
    keyword = text
    results = search_species(keyword)
    print("Résultats trouvés :", results)  # Vérifiez les données retournées
    return render(request, 'catalogue/search_results.html', {'results': results, 'keyword': keyword})

def catalogue_home(request):
    species_list = Species.objects.annotate(average_score=Avg('ratings__score'))  # Ajoute la moyenne des notes
    return render(request, 'catalogue/catalogue_home.html', {'species_list': species_list})

def species_detail(request, species_name):
    species = get_object_or_404(Species, name=species_name)
    return render(request, 'catalogue/species_detail.html', {'species': species})


def rate_species(request, species_id):
    species = get_object_or_404(Species, id=species_id)

    if request.method == "POST":
        score = int(request.POST.get('score'))
        rating, created = Rating.objects.update_or_create(
            user=request.user,
            species=species,
            defaults={'score': score}
        )
        # Afficher les informations dans la console
        print(f"L'utilisateur {request.user.username} a noté {species.name} avec un score de {score}.")
        return redirect('catalogue')  # Redirige vers la page du catalogue

    return render(request, 'catalogue/rate_species.html', {'species': species})
