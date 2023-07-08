from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Voetbalspeler(models.Model):    
    naam_speler = models.CharField(max_length=200)
    club = models.CharField(max_length=100)
    naam_auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datum_invoer = models.DateTimeField(default=timezone.now)
    datum_aanpassing = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.datum_aanpassing = timezone.now()
        self.save()

    def __str__(self):
        return self.naam_speler + " speelt bij " + self.club
 
