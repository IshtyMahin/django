from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from musician.models import Musician
# Create your models here.

class Album(models.Model):
    Album_name = models.CharField(max_length=100)
    Album_Musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    Album_release_date = models.DateField()
    Album_rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    
    def __str__(self):
        return self.Album_name