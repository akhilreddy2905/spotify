# music/admin.py

from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_name')
    fields = ('title', 'file_name', 'audio_file', 'cover_image')

admin.site.register(Song, SongAdmin)
