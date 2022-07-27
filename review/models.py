from django.db import models
from django.core.validators import MinLengthValidator
from bolshoi_cast.models import Artist

class Feedbacks(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,verbose_name='artist_name',default=1)
    rating = models.PositiveIntegerField()
    feedback = models.TextField()