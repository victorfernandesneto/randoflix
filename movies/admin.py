from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'watched', 'user')
    list_display_links = ['name']
    search_fields = ('user',)
    list_filter = ('user',)
