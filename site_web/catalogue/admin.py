from django.contrib import admin
from .models import Species

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'keywords','name_leaf','name_fruit','file_leaf','file_fruit','description','folder_gallery')
    list_editable = ('name', 'keywords','name_leaf','name_fruit','file_leaf','file_fruit','description','folder_gallery')
