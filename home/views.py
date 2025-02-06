from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import MovieReviewForm, SeriesReviewForm, MovieFilterForm, SeriesFilterForm
from .models import MovieList, MovieGenre, MovieReview, SeriesList, SeriesGenre, SeriesReview, SeasonList, Genre
from django.db.models import Count


def get_movie_and_reviews(tmdb_id):
    movie = get_object_or_404(MovieList, tmdb_id=tmdb_id)
    genres = MovieGenre.objects.filter(movie=movie).select_related('genre')
    reviews = MovieReview.objects.filter(movie=movie).order_by('-date_created')
    review_count = reviews.filter(approved=True).count()
    average_rating = movie.average_rating()
    return movie, genres, reviews, review_count, average_rating


def get_series_and_reviews(tmdb_id):
    series = get_object_or_404(SeriesList, tmdb_id=tmdb_id)
    genres = SeriesGenre.objects.filter(series=series).select_related('genre')
    reviews = SeriesReview.objects.filter(series=series).order_by('-date_created')
    review_count = reviews.filter(approved=True).count()
    average_rating = series.average_rating()
    return series, genres, reviews, review_count, average_rating


def handle_review_form(request, form, review, success_message, error_message, redirect_url):
    if form.is_valid() and review.user == request.user:
        review = form.save(commit=False)
        review.approved = False
        review.save()
        messages.add_message(request, messages.SUCCESS, success_message)
    else:
        messages.add_message(request, messages.ERROR, error_message)
    return HttpResponseRedirect(redirect_url)


def home(request):
    movies = MovieList.objects.all()[:25]
    series = SeriesList.objects.all().order_by('-first_air_date')[:25]
    return render(
        request,
        'home/index.html',
        {'movies': movies, 'series': series}
    )


def movies(request):
    movies = MovieList.objects.all()

    # Get genres associated with movies and order them alphabetically
    genres = Genre.objects.annotate(movie_count=Count('moviegenre')).filter(movie_count__gt=0).order_by('name')

    # Handle filters if present
    if request.method == "GET":
        form = MovieFilterForm(request.GET)
        form.fields['genre'].queryset = genres

        if form.is_valid():
            genre = form.cleaned_data.get('genre')
            min_rating = form.cleaned_data.get('min_rating')
            release_year = form.cleaned_data.get('release_year')

            if genre:
                movies = movies.filter(moviegenre__genre=genre)

            if min_rating:
                movies = movies.filter(moviereview__rating__gte=min_rating)

            if release_year:
                movies = movies.filter(release_date__year=release_year)
    else:
        form = MovieFilterForm()
        form.fields['genre'].queryset = genres

    return render(
        request,
        'home/movies.html',
        {'movies': movies, 'form': form}
    )


def series(request):
    series = SeriesList.objects.all().order_by('-first_air_date')

    # Get genres associated with series and order them alphabetically
    genres = Genre.objects.annotate(series_count=Count('seriesgenre')).filter(series_count__gt=0).order_by('name')

    # Handle filters if present
    if request.method == "GET":
        form = SeriesFilterForm(request.GET)
        form.fields['genre'].queryset = genres

        if form.is_valid():
            genre = form.cleaned_data.get('genre')
            first_air_date = form.cleaned_data.get('first_air_date')
            last_air_date = form.cleaned_data.get('last_air_date')
            number_of_seasons = form.cleaned_data.get('number_of_seasons')

            if genre:
                series = series.filter(seriesgenre__genre=genre)

            if first_air_date:
                series = series.filter(first_air_date__gte=first_air_date)

            if last_air_date:
                series = series.filter(last_air_date__lte=last_air_date)

            if number_of_seasons:
                series = series.filter(number_of_seasons=number_of_seasons)
    else:
        form = SeriesFilterForm()
        form.fields['genre'].queryset = genres

    return render(
        request,
        'home/series.html',
        {'series': series, 'form': form}
    )


def movie_detail(request, tmdb_id):
    movie, genres, reviews, review_count, average_rating = get_movie_and_reviews(tmdb_id)
    if request.user.is_authenticated:
        reviews = MovieReview.objects.filter(movie=movie).order_by('-date_created')
    else:
        reviews = reviews.filter(approved=True)

    if request.method == "POST":
        form = MovieReviewForm(request.POST, user=request.user, movie=movie)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review submitted successfully!')
            return HttpResponseRedirect(reverse('movie_detail', args=[movie.tmdb_id]))
        else:
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
    if request.method == "POST":
        movie = get_object_or_404(MovieList, tmdb_id=tmdb_id)
        review = get_object_or_404(MovieReview, pk=review_id)
        review_form = MovieReviewForm(data=request.POST, instance=review, user=request.user, movie=movie)
        return handle_review_form(
            request, review_form, review, 'Review Updated!', 'Error updating review!',
            reverse('movie_detail', args=[tmdb_id])
        )


def movie_review_delete(request, tmdb_id, review_id):
    movie = get_object_or_404(MovieList, tmdb_id=tmdb_id)
    review = get_object_or_404(MovieReview, pk=review_id)
    if review.user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review Deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Error deleting review!')
    return HttpResponseRedirect(reverse('movie_detail', args=[tmdb_id]))


def series_detail(request, tmdb_id):
    series, genres, reviews, review_count, average_rating = get_series_and_reviews(tmdb_id)
    seasons = SeasonList.objects.filter(series=series)  # Fetch seasons for the series
    if request.user.is_authenticated:
        reviews = SeriesReview.objects.filter(series=series).order_by('-date_created')
    else:
        reviews = reviews.filter(approved=True)

    if request.method == "POST":
        form = SeriesReviewForm(request.POST, user=request.user, series=series)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.series = series
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review submitted successfully!')
            return HttpResponseRedirect(reverse('series_detail', args=[series.tmdb_id]))
        else:
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
            'genres': genres,
            'reviews': reviews,
            'review_count': review_count,
            'average_rating': average_rating,
            'form': form,
            'user': request.user,
            'seasons': seasons  # Pass seasons to the template
        }
    )


def series_review_edit(request, tmdb_id, review_id):
    if request.method == "POST":
        series = get_object_or_404(SeriesList, tmdb_id=tmdb_id)
        review = get_object_or_404(SeriesReview, pk=review_id)
        review_form = SeriesReviewForm(data=request.POST, instance=review, user=request.user, series=series)
        return handle_review_form(
            request, review_form, review, 'Review Updated!', 'Error updating review!',
            reverse('series_detail', args=[tmdb_id])
        )


def series_review_delete(request, tmdb_id, review_id):
    series = get_object_or_404(SeriesList, tmdb_id=tmdb_id)
    review = get_object_or_404(SeriesReview, pk=review_id)
    if review.user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review Deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Error deleting review!')
    return HttpResponseRedirect(reverse('series_detail', args=[tmdb_id]))


def search_results(request):
    query = request.GET.get('q')
    movies = MovieList.objects.filter(title__icontains=query)
    series = SeriesList.objects.filter(title__icontains=query)
    return render(
        request,
        'home/search_results.html',
        {'query': query, 'movies': movies, 'series': series}
    )
