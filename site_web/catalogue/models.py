from django.db import models
from catalogue import fruit_photos
from django import forms

class Species(models.Model):
    name = models.CharField(max_length=200, unique=True)
    name_leaf = models.CharField(max_length=200, blank=True)
    #j'ai retire unique = True car ca ne me permettait pas de
    # migrate
    name_fruit = models.CharField(max_length=200, blank=True)
    file_leaf = models.CharField(max_length=200, unique=True, blank=True)
    file_fruit = models.CharField(max_length=200, unique=True, blank=True)
    description = models.CharField(max_length=100000, unique=True, blank=True)
    folder_gallery = models.CharField(max_length=200, unique=True, blank=True)
    keywords = models.CharField(max_length=1000, unique=False, blank=True)


    def __str__(self):
        return f"Species(name={self.name}, name_leaf={self.name_leaf}, name_fruit={self.name_fruit}, " \
               f"file_leaf={self.file_leaf}, file_fruit={self.file_fruit}, " \
               f"description={self.description[:50]}..., folder_gallery={self.folder_gallery}, " \
               f"keywords={self.keywords})"