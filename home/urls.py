from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies, name='movies'),
    path('series/', views.series, name='series'),
    path('movie/<int:tmdb_id>/', views.movie_detail, name='movie_detail'),
    path(
        'movie/<int:tmdb_id>/edit_review/<int:review_id>/',
        views.review_edit, name='edit_review'
    ),
]
