from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Species
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
import random
from django.db.models import Avg


def catalogue_feuilles(request):
    feuilles = Species.objects.exclude(file_leaf="")
    images = [{'type': 'Feuilles', 'path': feuille.file_leaf, 'id': feuille.id, 'portfolio_id':'portfolioModal'+str(feuille.id)} for feuille in feuilles]
    return render(request, 'catalogue/catalogue_feuilles.html', {'images' : images})
    

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

def quiz_view(request):
    # Initialiser le quiz si nécessaire
    if 'quiz_score' not in request.session:
        request.session['quiz_score'] = 0
        request.session['quiz_round'] = 1
        request.session['asked_species'] = []  # Liste des espèces déjà posées

    # Fin du quiz après 5 tours
    if request.session['quiz_round'] > 5:
        score = request.session['quiz_score']
        request.session.flush()  # Réinitialise le quiz
        return render(request, 'catalogue/quiz_result.html', {'score': score})
    
    # S'assurer que 'asked_species' est initialisée
    if 'asked_species' not in request.session:
        request.session['asked_species'] = []
    
    # Récupérer toutes les espèces et exclure celles déjà posées
    species_list = Species.objects.exclude(id__in=request.session['asked_species'])

    if not species_list.exists():
        # Si toutes les espèces ont été utilisées
        score = request.session['quiz_score']
        request.session.flush()  # Réinitialise le quiz
        return render(request, 'catalogue/quiz_result.html', {'score': score})

    # Sélectionner une espèce aléatoire
    correct_species = random.choice(list(species_list))

    # Ajouter l'espèce posée à la liste des espèces déjà posées
    asked_species = request.session['asked_species']
    asked_species.append(correct_species.id)
    request.session['asked_species'] = asked_species
    
    # Alterner entre feuille et fruit
    if request.session['quiz_round'] % 2 == 1:  # Tour impair : image de feuille
        image = f"/{correct_species.file_leaf}"
    else:  # Tour pair : image de fruit
        image = f"/{correct_species.file_fruit}"

    # Générer des options de réponse sans inclure des doublons
    other_species = random.sample(
        [s for s in Species.objects.exclude(id=correct_species.id)],
        min(3, Species.objects.count() - 1)
    )
    options = [correct_species] + other_species
    random.shuffle(options)

    # Préparer le contexte
    context = {
        'image': image, 
        'options': options,
        'correct_id': correct_species.id,
        'round': request.session['quiz_round'],
        'score': request.session['quiz_score'],
    }

    # Vérifier la réponse précédente
    if request.method == 'POST':
        selected_id = int(request.POST.get('selected_id'))
        correct_id = int(request.POST.get('correct_id'))
        if selected_id == correct_id:
            request.session['quiz_score'] += 1
        request.session['quiz_round'] += 1
        return redirect('quiz')

    return render(request, 'catalogue/quiz.html', context)

def species_detail(request, species_name):
    species = get_object_or_404(Species, name=species_name)
    return redirect('/description/'+str(species.id))