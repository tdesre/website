from django.test import TestCase
from django.urls import reverse
from .models import Species

class MyPageTests(TestCase):
    
    def test_catalogue_feuilles(self):
        response = self.client.get(reverse('catalogue_feuilles'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Feuilles")
    
    def test_catalogue_fruits(self):
        response = self.client.get(reverse('catalogue_fruits'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fruits")  # Remplacez par un contenu spécifique à cette page.
    
    def test_species_search_view(self):
        response = self.client.get(reverse('species_search', args=["mot-clé1"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/search_results.html')
        self.assertEqual(len(response.context['results']), 0)
         

    # Test de contenu dynamique
    def test_page_contains_dynamic_content(self):
        response = self.client.get(reverse('accueil'))
        self.assertContains(response, 'accueil/accueil.css')  # Vérifie la présence d'un contenu dynamique
        self.assertContains(response, '/static/accueil/images/logo.png')

    def test_bouton_feuilles_lien(self):
        # Accède à la page d'accueil
        response = self.client.get(reverse('accueil'))
        # Vérifie que l'URL /catalogue/feuilles/ est présente dans le HTML
        self.assertContains(response, 'href="/catalogue/feuilles/"')

    def test_navigation_vers_catalogue_feuilles(self):
        # Simule un accès direct à la page /catalogue/feuilles/
        url_feuilles = reverse('catalogue_feuilles')  # Génère l'URL cible
        response = self.client.get(url_feuilles)
        # Vérifie que la page de destination retourne un code 200
        self.assertEqual(response.status_code, 200)

    def test_bouton_fruits_lien(self):
        # Accède à la page d'accueil
        response = self.client.get(reverse('accueil'))
        # Vérifie que l'URL /catalogue/feuilles/ est présente dans le HTML
        self.assertContains(response, 'href="/catalogue/fruits/"')

    def test_navigation_vers_catalogue_fruits(self):
        # Simule un accès direct à la page /catalogue/feuilles/
        url_fruits = reverse('catalogue_fruits')  # Génère l'URL cible
        response = self.client.get(url_fruits)
        # Vérifie que la page de destination retourne un code 200
        self.assertEqual(response.status_code, 200)   


    def test_quiz_start(self):
        """
        Tester si le quiz démarre correctement.
        """
        response = self.client.get(reverse('quiz'))
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "Question 1")
        #self.assertIn('image', response.context)
        #self.assertIn('options', response.context)

    def test_quiz_end(self):
        """
        Tester la fin du quiz après 5 questions.
        """
        session = self.client.session
        session['quiz_round'] = 6  # Simule une session au-delà du dernier round
        session['quiz_score'] = 4
        session.save()

        response = self.client.get(reverse('quiz'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Vous avez terminé le quiz avec un score de : 4/5")  # Vérifier la fin du quiz
    
    

    