from django.db import models

# Create your models here.
class Lugat(models.Model):
    english = models.CharField(max_length=200)
    uzbek = models.CharField(max_length=200)

    def __str__(self):
        return self.english