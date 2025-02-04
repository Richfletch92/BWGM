from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import MovieReviewForm, SeriesReviewForm
from .models import MovieList, SeriesList, MovieGenre, MovieReview, SeriesReview


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
    reviews = MovieReview.objects.filter(
        movie=movie, approved=True
    ).order_by('-date_created')
    review_count = reviews.count()
    average_rating = movie.average_rating()

    if request.user.is_authenticated:
        reviews = MovieReview.objects.filter(
            movie=movie
        ).order_by('-date_created')
    else:
        reviews = MovieReview.objects.filter(
            movie=movie, approved=True
        ).order_by('-date_created')

    if request.method == "POST":
        form = MovieReviewForm(request.POST, user=request.user, movie=movie)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            messages.add_message(
                request, messages.SUCCESS, 'Review submitted successfully!'
            )
            return HttpResponseRedirect(
                reverse('movie_detail', args=[movie.tmdb_id])
            )
        else:
            # Add each error as a separate message
            for errors in form.errors.values():
                for error in errors:
                    messages.add_message(request, messages.ERROR, error)
    else:
        form = MovieReviewForm(user=request.user, movie=movie)

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


def movie_review_edit(request, tmdb_id, review_id):
    """
    View to edit reviews
    """
    if request.method == "POST":
        queryset = MovieList.objects.all()
        movie = get_object_or_404(queryset, tmdb_id=tmdb_id)
        review = get_object_or_404(MovieReview, pk=review_id)
        review_form = MovieReviewForm(
            data=request.POST,
            instance=review,
            user=request.user,
            movie=movie
        )

        if review_form.is_valid() and review.user == request.user:
            review = review_form.save(commit=False)
            review.movie = movie
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating review!'
            )

    return HttpResponseRedirect(reverse('movie_detail', args=[tmdb_id]))


def movie_review_delete(request, tmdb_id, review_id):
    """
    View to delete reviews
    """
    queryset = MovieList.objects.all()
    movie = get_object_or_404(queryset, tmdb_id=tmdb_id)
    review = get_object_or_404(MovieReview, pk=review_id)
    
    if review.user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review Deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'Error deleting review!'
        )

    return HttpResponseRedirect(reverse('movie_detail', args=[tmdb_id]))


def series_detail(request, tmdb_id):
    queryset = SeriesList.objects.all()
    series = get_object_or_404(queryset, tmdb_id=tmdb_id)
    reviews = SeriesReview.objects.filter(
        series=series, approved=True
    ).order_by('-date_created')
    review_count = reviews.count()
    average_rating = series.average_rating()

    if request.user.is_authenticated:
        reviews = SeriesReview.objects.filter(
            series=series
        ).order_by('-date_created')
    else:
        reviews = SeriesReview.objects.filter(
            series=series, approved=True
        ).order_by('-date_created')

    if request.method == "POST":
        form = SeriesReviewForm(request.POST, user=request.user, series=series)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.series = series
            review.save()
            messages.add_message(
                request, messages.SUCCESS, 'Review submitted successfully!'
            )
            return HttpResponseRedirect(
                reverse('series_detail', args=[series.tmdb_id])
            )
        else:
            # Add each error as a separate message
            for errors in form.errors.values():
                for error in errors:
                    messages.add_message(request, messages.ERROR, error)
    else:
        form = SeriesReviewForm(user=request.user, series=series)

    return render(
        request,
        'home/series_detail.html',
        {
            'series': series,
            'reviews': reviews,
            'review_count': review_count,
            'average_rating': average_rating,
            'form': form,
            'user': request.user
        }
    )


def series_review_edit(request, tmdb_id, review_id):
    """
    View to edit reviews
    """
    if request.method == "POST":
        queryset = SeriesList.objects.all()
        series = get_object_or_404(queryset, tmdb_id=tmdb_id)
        review = get_object_or_404(SeriesReview, pk=review_id)
        review_form = SeriesReviewForm(
            data=request.POST,
            instance=review,
            user=request.user,
            series=series
        )

        if review_form.is_valid() and review.user == request.user:
            review = review_form.save(commit=False)
            review.series = series
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating review!'
            )

    return HttpResponseRedirect(reverse('series_detail', args=[tmdb_id]))

def series_review_delete(request, tmdb_id, review_id):
    """
    View to delete reviews
    """
    queryset = SeriesList.objects.all()
    series = get_object_or_404(queryset, tmdb_id=tmdb_id)
    review = get_object_or_404(SeriesReview, pk=review_id)
    
    if review.user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review Deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'Error deleting review!'
        )

    return HttpResponseRedirect(reverse('series_detail', args=[tmdb_id]))
