from django.test import TestCase
from django.urls import reverse

class MyPageTests(TestCase):
    
    # Test de la réponse HTTP
    def test_page_status_code(self):
        response = self.client.get(reverse('accueil'))  # Remplacez par le nom de votre vue
        self.assertEqual(response.status_code, 200)  # Vérifie le code de statut HTTP (200 OK)

    # Test de la présence d'un élément HTML
    def test_page_contains_specific_element(self):
        response = self.client.get(reverse('accueil'))
        self.assertContains(response, '<h1 class="site-name">Catalogue Botanique</h1>')  # Vérifie qu'un titre est présent
        self.assertContains(response, '<h1>Bienvenue sur notre site</h1>')
        

    # Test de contenu dynamique
    def test_page_contains_dynamic_content(self):
        response = self.client.get(reverse('accueil'))
        self.assertContains(response, 'accueil/accueil.css')  # Vérifie la présence d'un contenu dynamique
        self.assertContains(response, 'accueil/images/logo.jpg')

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