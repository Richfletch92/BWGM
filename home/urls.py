from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies, name='movies'),
    path('series/', views.series, name='series'),
    path('movie/<int:tmdb_id>/', views.movie_detail, name='movie_detail'),
    path(
        'movie/<int:tmdb_id>/edit_review/<int:review_id>/',
        views.movie_review_edit, name='edit_review'
    ),
    path(
        'movie/<int:tmdb_id>/delete_review/<int:review_id>/',
        views.movie_review_delete, name='delete_review'
    ),
    path(
        'series/<int:tmdb_id>/', views.series_detail, name='series_detail'
    ),
    path(
        'series/<int:tmdb_id>/edit_review/<int:review_id>/',
        views.series_review_edit, name='edit_series_review'
    ),
    path(
        'series/<int:tmdb_id>/delete_review/<int:review_id>/',
        views.series_review_delete, name='delete_series_review'
    ),
    path('search/', views.search_results, name='search_results'),
]
