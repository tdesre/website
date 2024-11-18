from django.shortcuts import render
from django.db.models import Q
from .models import Species
from django.http import HttpResponse

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
'''
     # Construire manuellement le contenu HTML
    response_content = f"<h1>Résultats de la recherche pour '{keyword}'</h1>"
    
    if results:
        response_content += "<ul>"
        for species_name in results:
            response_content += f"<li>{species_name}</li>"
        response_content += "</ul>"
    else:
        response_content += f"<p>Aucun résultat trouvé pour '{keyword}'</p>"
    
    # Retourner une réponse HTTP avec le contenu HTML
    return HttpResponse(response_content)
    
'''

