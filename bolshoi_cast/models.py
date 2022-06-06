from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    sphere = models.CharField(max_length=60)
    position = models.CharField(max_length=60)
    photo = models.CharField(max_length=20000,default=50,null=True)

    def __str__(self):
        return f'{self.name},{self.surname},{self.sphere},{self.position}{self.photo}'

