from django.contrib import admin
from .models import MovieList, SeriesList, MovieReview
from django_summernote.admin import SummernoteModelAdmin


@admin.register(MovieList)
class MovieListAdmin(SummernoteModelAdmin):
    # Customize list display
    list_display = ('title', 'release_date', 'get_average_rating')
    search_fields = ('title',)  # Add search functionality
    list_filter = ('release_date',)  # Add filters
    summernote_fields = 'description'  # Use Summernote editor for description
    ordering = ('-release_date',)  # Default ordering
    readonly_fields = ('tmdb_id',)  # Make tmdb_id read-only
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'poster_path')
        }),
        ('Additional Info', {
            'fields': ('release_date', 'runtime', 'get_average_rating')
        }),
    )

    def get_average_rating(self, obj):
        return obj.average_rating()
    get_average_rating.short_description = 'Average Rating'


@admin.register(SeriesList)
class SeriesListAdmin(SummernoteModelAdmin):
    # Customize list display
    list_display = ('title', 'first_air_date', 'get_average_rating')
    search_fields = ('title',)  # Add search functionality
    list_filter = ('first_air_date',)  # Add filters
    summernote_fields = 'description'  # Use Summernote editor for description
    ordering = ('-first_air_date',)  # Default ordering
    readonly_fields = ('tmdb_id',)  # Make tmdb_id read-only
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'poster_path')
        }),
        ('Additional Info', {
            'fields': (
                'first_air_date',
                'last_air_date',
                'number_of_seasons',
                'get_average_rating'
            )
        }),
    )

    def get_average_rating(self, obj):
        return obj.average_rating()
    get_average_rating.short_description = 'Average Rating'


admin.site.register(MovieReview)
