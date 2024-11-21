from django.test import TestCase
from django.urls import reverse
from catalogue.models import Species
import os
from unittest.mock import patch

class SpeciesViewsTests(TestCase):
    
    def setUp(self):
        # Créer une espèce de test pour les vues description et localisation
        self.species1 = Species.objects.create(
            name="Espèce 1",
            folder_gallery="catalogue/gallery",  
            description="test_description.txt",
            file_leaf="leaf1.jpg",
            file_fruit="fruit1.jpg"
        )


    def test_description_view_valid_id(self):
        #Test de la vue description avec un ID valide
        response = self.client.get(reverse('description', kwargs={'id': self.species1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Espèce 1")  # Vérifier que le nom de l'espèce est présent

