from django.db import models
from django.contrib.auth.models import User  # Utilisé pour associer les notes aux utilisateurs

class Species(models.Model):
    name = models.CharField(max_length=200, unique=True)
    name_leaf = models.CharField(max_length=200, unique=True, blank=True)
    name_fruit = models.CharField(max_length=200, unique=True, blank=True)
    file_leaf = models.CharField(max_length=200, unique=True, blank=True)
    file_fruit = models.CharField(max_length=200, unique=True, blank=True)
    description = models.CharField(max_length=100000, unique=True, blank=True)
    folder_gallery = models.CharField(max_length=200, unique=True, blank=True)
    keywords = models.CharField(max_length=1000, unique=False, blank=True)
    

    def average_rating(self):
        # Calcule la moyenne des notes pour cette espèce
        ratings = self.ratings.all()  # Accède à tous les Ratings liés à cette espèce
        if ratings.exists():
            return sum(rating.score for rating in ratings) / ratings.count()
        return None

    def __str__(self):
        return f"Nom de l'espèce : {self.name}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur qui donne la note
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='ratings')  # Espèce notée
    score = models.IntegerField()  # Note donnée par l'utilisateur

    class Meta:
        unique_together = ('user', 'species')  # Empêche un utilisateur de noter la même espèce plusieurs fois

    def __str__(self):
        return f"{self.user.username} - {self.species.name} : {self.score}"