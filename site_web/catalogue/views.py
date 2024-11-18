from django.shortcuts import render, redirect
import random
from django.db.models import Q
from .models import Species
from django.http import HttpResponse
from django.template import loader

def catalogue_feuilles(request):
    feuilles = Species.objects.exclude(name_leaf="").all()
    context = {'species_list': feuilles, 'type': 'Feuilles'}
    return render(request, 'catalogue/catalogue.html', context)

def search_species(keyword):
    # Utilisation de Q pour construire la requête de recherche
    query = Q(keywords__icontains=keyword) | Q(name_leaf__icontains=keyword) | Q(name_fruit__icontains=keyword)
    
    # Filtrer les résultats en fonction de la requête
    results = Species.objects.filter(query)
    
    # Retourner les résultats (par exemple, les noms des espèces trouvées)
    return results.values_list('name', flat=True)  # Renvoie une liste de noms d'espèces


def species_search_view(request, text):
    keyword = text
    results = search_species(keyword)
    print ("abs")
    return render(request, 'catalogue/search_results.html', {'results': results, 'keyword': keyword})


def catalogue_home(request):
    return render(request, 'catalogue/catalogue_home.html')

def quiz_view(request):
    # Vérifier si le quiz est déjà en cours
    if 'quiz_score' not in request.session:
        request.session['quiz_score'] = 0
        request.session['quiz_round'] = 1

    # Fin du quiz après 5 tours
    if request.session['quiz_round'] > 5:
        score = request.session['quiz_score']
        request.session.flush()  # Réinitialise le quiz
        return render(request, 'catalogue/quiz_result.html', {'score': score})

    # Sélectionner une espèce aléatoire
    species_list = list(Species.objects.all())
    correct_species = random.choice(species_list)
    # Générer des options de réponse
    other_species = random.sample(species_list, min(3, len(species_list)))
    options = [correct_species] + other_species
    random.shuffle(options)
    # Afficher l'image et les options
    context = {
        'image': correct_species.file_leaf,  # Change en `file_fruit` si nécessaire
        'options': options,
        'correct_id': correct_species.id,
        'round': request.session['quiz_round'],
        'score': request.session['quiz_score'],}
    # Vérifier la réponse précédente
    if request.method == 'POST':
        selected_id = int(request.POST.get('selected_id'))
        if selected_id == request.POST.get('correct_id'):
            request.session['quiz_score'] += 1
        request.session['quiz_round'] += 1
        return redirect('quiz')  # Passe au tour suivant

    return render(request, 'catalogue/quiz.html', context)

