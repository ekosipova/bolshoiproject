from django.contrib import admin
from .models import Feedbacks


@admin.register(Feedbacks)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id','rating','feedback','artist_id']
    list_editable = ['rating','feedback']
    ordering = ['id']
    list_per_page = 25