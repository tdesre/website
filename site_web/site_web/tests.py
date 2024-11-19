from django.test import TestCase
import os

class ASGIandWSGITest(TestCase):
    
    def test_asgi_application(self):
        # Vérifier que l'application ASGI est configurée correctement
        from site_web.asgi import application
        self.assertIsNotNone(application)
    
    def test_wsgi_application(self):
        # Vérifier que l'application WSGI est configurée correctement
        from site_web.wsgi import application
        self.assertIsNotNone(application)