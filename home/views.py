from django.shortcuts import render
from .models import MovieList, SeriesList


def home(request):
    movies = MovieList.objects.all()[:25]
    series = SeriesList.objects.all()[:25]
    return render(
        request,
        'home/index.html',
        {'movies': movies, 'series': series}
    )


def movies(request):
    movies = MovieList.objects.all()
    return render(
        request,
        'home/movies.html',
        {'movies': movies}
    )


def series(request):
    series = SeriesList.objects.all()
    return render(
        request,
        'home/series.html',
        {'series': series}
    )