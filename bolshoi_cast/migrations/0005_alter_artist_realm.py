# Generated by Django 4.0.3 on 2022-06-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolshoi_cast', '0004_rename_sphere_artist_realm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='realm',
            field=models.CharField(choices=[('Б', 'Баллет'), ('О', 'Опера'), ('ОР', 'Оркестр')], default='Б', max_length=2),
        ),
    ]
