from django.db import models
from catalogue import fruit_photos
from django import forms

class Species(models.Model):
    name = models.CharField(max_length=200, unique=True)
    name_leaf = models.CharField(max_length=200, unique=False, blank=True)
    name_fruit = models.CharField(max_length=200, unique=False, blank=True)
    file_leaf = models.CharField(max_length=200, unique=False, blank=True)
    file_fruit = models.CharField(max_length=200, unique=False, blank=True)
    description = models.CharField(max_length=100000, unique=False, blank=True)
    folder_gallery = models.CharField(max_length=200, unique=False, blank=True)
    keywords = models.CharField(max_length=1000, unique=False, blank=True)



class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False, label="Recherche")