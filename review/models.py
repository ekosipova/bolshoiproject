from django.db import models
from django.core.validators import MinLengthValidator

class Feedback(models.Model):
    CHOICES = [
        ('Балет','Балет'),
        ('Опера', 'Опера'),
        ('Оркестр','Оркестр')
    ]
    realm = models.CharField(max_length=40,choices=CHOICES,default='Балет')
    name = models.CharField(max_length=100,validators=[MinLengthValidator(2)])
    rating = models.PositiveIntegerField()
    feedback = models.TextField()