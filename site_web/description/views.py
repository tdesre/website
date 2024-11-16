from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.forms.models import model_to_dict
from catalogue.models import Species

def description(request, id):
    if id == 0 :
        return redirect('/description/1')
    if id > Species.objects.count():
        return redirect('/description/'+str(Species.objects.count()))
    
    species = get_object_or_404(Species, id=id)
    images = [{'full': f'description/images/fulls/{i:02}.jpg', 'thumb': f'description/images/thumbs/{i:02}.jpg', 'title': f'Title {i}', 'desc': f'Description for image {i}'} for i in range(1, 5)]
    context= {**model_to_dict(species), 'images': images}

    return render(request, 'description/description.html', context)

def error(request, text):
    return HttpResponse("URL incorrecte : entrer un nombre entre 1 et "+str(Species.objects.count()))