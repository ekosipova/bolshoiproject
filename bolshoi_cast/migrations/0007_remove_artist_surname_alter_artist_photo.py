# Generated by Django 4.0.3 on 2022-06-08 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolshoi_cast', '0006_alter_artist_position_alter_artist_realm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='surname',
        ),
        migrations.AlterField(
            model_name='artist',
            name='photo',
            field=models.CharField(blank=True, default=50, max_length=20000, null=True),
        ),
    ]