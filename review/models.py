from django.db import models

class Feedback(models.Model):
    realm = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    feedback = models.TextField()
