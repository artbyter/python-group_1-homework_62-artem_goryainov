from django.contrib import admin
from .models import Movie


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'release_date']
    ordering = ['-release_date']
    search_fields = ['name', 'id']


admin.site.register(Movie, MovieAdmin)
