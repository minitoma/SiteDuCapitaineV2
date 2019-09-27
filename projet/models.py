from django.db import models
from django.utils import timezone

# Create your models here.

class Projet(models.Model):
    #projet_id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=30)
    description = models.TextField()
    url = models.URLField(blank=True)
    published_date = models.DateTimeField()
    info = "test"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titre

class ProjetImage(models.Model):
    projet = models.ForeignKey(Projet, related_name='images', on_delete=models.CASCADE )
    image = models.ImageField(blank=True)
