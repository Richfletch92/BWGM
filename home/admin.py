from django.contrib import admin
from .models import MovieList, SeriesList, MovieReview, SeriesReview
from django_summernote.admin import SummernoteModelAdmin


def approve_reviews(modeladmin, request, queryset):
    """
    Custom admin action to approve selected reviews.
    """
    queryset.update(approved=True)
    modeladmin.message_user(request, "Selected reviews have been approved.")


approve_reviews.short_description = "Approve selected reviews"


def unapprove_reviews(modeladmin, request, queryset):
    """
    Custom admin action to unapprove selected reviews.
    """
    queryset.update(approved=False)
    modeladmin.message_user(request, "Selected reviews have been unapproved.")


unapprove_reviews.short_description = "Unapprove selected reviews"


@admin.register(MovieList)
class MovieListAdmin(SummernoteModelAdmin):
    """
    Admin interface for MovieList model.
    """
    list_display = ('title', 'release_date', 'get_average_rating')
    search_fields = ('title',)
    list_filter = ('release_date',)
    summernote_fields = 'description'
    ordering = ('-release_date',)
    readonly_fields = ('tmdb_id',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'poster_path')
        }),
        ('Additional Info', {
            'fields': ('release_date', 'runtime', 'get_average_rating')
        }),
    )

    def get_average_rating(self, obj):
        """
        Custom method to get the average rating of a movie.
        """
        return obj.average_rating()
    get_average_rating.short_description = 'Average Rating'


@admin.register(SeriesList)
class SeriesListAdmin(SummernoteModelAdmin):
    """
    Admin interface for SeriesList model.
    """
    list_display = ('title', 'first_air_date', 'get_average_rating')
    search_fields = ('title',)
    list_filter = ('first_air_date',)
    summernote_fields = 'description'
    ordering = ('-first_air_date',)
    readonly_fields = ('tmdb_id',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'poster_path')
        }),
        ('Additional Info', {
            'fields': (
                'first_air_date', 'last_air_date', 'number_of_seasons',
                'get_average_rating'
            )
        }),
    )

    def get_average_rating(self, obj):
        """
        Custom method to get the average rating of a series.
        """
        return obj.average_rating()
    get_average_rating.short_description = 'Average Rating'


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    """
    Admin interface for MovieReview model.
    """
    list_display = ('movie', 'user', 'rating', 'date_created', 'approved')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('approved', 'date_created')
    ordering = ('-date_created',)
    actions = [approve_reviews, unapprove_reviews]


@admin.register(SeriesReview)
class SeriesReviewAdmin(admin.ModelAdmin):
    """
    Admin interface for SeriesReview model.
    """
    list_display = ('series', 'user', 'rating', 'date_created', 'approved')
    search_fields = ('user__username', 'series__title')
    list_filter = ('approved', 'date_created')
    ordering = ('-date_created',)
    actions = [approve_reviews, unapprove_reviews]
