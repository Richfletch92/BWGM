from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import MovieList, SeriesList, MovieGenre, MovieReview


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


def movie_detail(request, tmdb_id):
    queryset = MovieList.objects.all()
    movie = get_object_or_404(queryset, tmdb_id=tmdb_id)
    genres = MovieGenre.objects.filter(movie=movie).select_related('genre')
    reviews = MovieReview.objects.filter(movie=movie, approved=True).order_by('-date_created')
    review_count = reviews.count()
    average_rating = movie.average_rating()

    if request.user.is_authenticated:
        reviews = MovieReview.objects.filter(movie=movie).order_by('-date_created')
    else:
        reviews = MovieReview.objects.filter(movie=movie, approved=True).order_by('-date_created')

    if request.method == "POST":
        form = ReviewForm(request.POST, user=request.user, movie=movie)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review submitted successfully!')
            return HttpResponseRedirect(reverse('movie_detail', args=[movie.tmdb_id]))
        else:
            for error in form.errors.values():
                messages.add_message(request, messages.ERROR, error)
    else:
        form = ReviewForm(user=request.user, movie=movie)

    return render(
        request,
        'home/movie_detail.html',
        {
            'movie': movie,
            'genres': genres,
            'reviews': reviews,
            'review_count': review_count,
            'average_rating': average_rating,
            'form': form,
            'user': request.user
        }
    )


def review_edit(request, review_id):
    review = get_object_or_404(MovieReview, id=review_id)
    if request.user == review.user:
        if request.method == "POST":
            form = ReviewForm(data=request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Review updated successfully!')
                return HttpResponseRedirect(reverse('movie_detail', args=[review.movie.tmdb_id]))
            else:
                for error in form.errors.values():
                    messages.add_message(request, messages.ERROR, error)
        form = ReviewForm(instance=review)
        return render(
            request,
            'home/review_edit.html',
            {'form': form, 'review': review}
        )
    else:
        messages.add_message(request, messages.ERROR, 'You are not authorized to edit this review!')
        return HttpResponseRedirect(reverse('movie_detail', args=[review.movie.tmdb_id]))