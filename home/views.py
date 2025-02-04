from django.shortcuts import render, get_object_or_404, reverse
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
        form = ReviewForm(request.POST, user=request.user, movie=movie)
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


def review_edit(request, tmdb_id, review_id):
    """
    View to edit reviews
    """
    if request.method == "POST":
        queryset = MovieList.objects.all()
        movie = get_object_or_404(queryset, tmdb_id=tmdb_id)
        review = get_object_or_404(MovieReview, pk=review_id)
        review_form = ReviewForm(
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


def review_delete(request, tmdb_id, review_id):
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
