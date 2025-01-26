from django.shortcuts import render
from django.views import generic
from .models import Movie

# class MovieList(generic.ListView):
#     queryset = Movie.objects.all()
#     template_name = 'movies/index.html'
#     context_object_name = 'movies'


def index(request):
    movies = Movie.objects.order_by('-release_date')[:20]
    return render(request, 'movies/index.html', {'movies': movies})