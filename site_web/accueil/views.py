from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def accueil(request):

   template = loader.get_template("./accueil/accueil.html")
   return HttpResponse(template.render(request=request))