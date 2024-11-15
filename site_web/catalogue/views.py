from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def catalogue(request):

   template = loader.get_template("./catalogue/catalogue.html")
   return HttpResponse(template.render(request=request))
