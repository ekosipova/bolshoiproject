from django.db import models

class Artist(models.Model):
    REALM_CHOICES = [
        ('Балет','Балет'),
        ('Опера','Опера'),
        ('Оркестр','Оркестр')
    ]
    POSITION_CHOICES = [
        ('Балерины','Балерины'),
        ('Премьеры','Премьеры'),
        ('Ведущие солистки','Ведущие солистки'),
        ('Ведущие солисты','Ведущие солисты'),
        ('Первые солистки','Первые солистки'),
        ('Первые солисты','Первые солисты'),
        ('Солистки','Солистки'),
        ('Солисты','Солисты'),
        ('Сопрано','Сопрано'),
        ('Меццо-сопрано','Меццо-сопрано'),
        ('Теноры','Теноры'),
        ('Баритоны','Баритоны'),
        ('Бассы','Бассы'),
        ('Дирижеры','Дирижеры'),
        ('Хор','Хор')
        ]
    name = models.CharField(max_length=60)
    realm = models.CharField(max_length=40,choices=REALM_CHOICES,default='Балет')
    position = models.CharField(max_length=40, choices=POSITION_CHOICES, default='Балерины')
    photo = models.CharField(max_length=20000,default=50,null=True,blank=True)

    def __str__(self):
        return f'{self.name},{self.realm},{self.position}{self.photo}'

