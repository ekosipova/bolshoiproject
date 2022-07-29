from django.db import models
from bolshoi_cast.models import Artist
from django.core.validators import MaxValueValidator, MinValueValidator

class Feedbacks(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,verbose_name='artist_name',default=1)
    rating = models.PositiveIntegerField(default=1,max_length=1,validators=[MaxValueValidator(5),MinValueValidator(1)])
    feedback = models.TextField()