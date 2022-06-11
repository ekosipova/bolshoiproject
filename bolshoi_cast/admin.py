from django.contrib import admin
from .models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id','name','realm','position']
    list_editable = ['name','realm','position']
    ordering = ['id']
    list_per_page = 25