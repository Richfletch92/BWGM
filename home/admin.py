from django.contrib import admin
from .models import MovieList, SeriesList
from django_summernote.admin import SummernoteModelAdmin

@admin.register(MovieList)
class MovieListAdmin(SummernoteModelAdmin):
    list_display = ('title', 'release_date', 'average_rating')  # Customize list display
    search_fields = ('title',)  # Add search functionality
    list_filter = ('release_date', 'average_rating')  # Add filters
    summernote_fields = 'description'  # Use Summernote editor for description
    ordering = ('-release_date',)  # Default ordering
    readonly_fields = ('tmdb_id',)  # Make tmdb_id read-only
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'poster_path')
        }),
        ('Additional Info', {
            'fields': ('release_date', 'runtime', 'average_rating')
        }),
    )

@admin.register(SeriesList)
class SeriesListAdmin(SummernoteModelAdmin):
    list_display = ('title', 'first_air_date', 'average_rating')  # Customize list display
    search_fields = ('title',)  # Add search functionality
    list_filter = ('first_air_date', 'average_rating')  # Add filters
    summernote_fields = 'description'  # Use Summernote editor for description
    ordering = ('-first_air_date',)  # Default ordering
    readonly_fields = ('tmdb_id',)  # Make tmdb_id read-only
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'poster_path')
        }),
        ('Additional Info', {
            'fields': ('first_air_date', 'last_air_date', 'number_of_seasons', 'average_rating')
        }),
    )
