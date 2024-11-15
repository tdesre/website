from django.shortcuts import render, get_object_or_404
from catalogue.models import Species

def item_detail(request, item_id):
    # Récupération de l'espèce avec l'ID fourni
    species = get_object_or_404(Species, id=item_id)
    context = {'species': species}
    return render(request, 'description/detail.html', context)
