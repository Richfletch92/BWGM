from .models import MovieReview, SeriesReview, Genre
from django import forms
from django.core.exceptions import ValidationError


class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 11)]),
            'content': forms.Textarea(attrs={'rows': 5})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.movie = kwargs.pop('movie', None)
        super().__init__(*args, **kwargs)

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if self.instance.pk:
            # Exclude the current review from the validation check
            if MovieReview.objects.filter(
                user=self.user, movie=self.movie, content=content
            ).exclude(pk=self.instance.pk).exists():
                raise ValidationError(
                    "You have already submitted a review with the same "
                    "content."
                )
        else:
            if MovieReview.objects.filter(
                user=self.user, movie=self.movie, content=content
            ).exists():
                raise ValidationError(
                    "You have already submitted a review with the same "
                    "content."
                )
        return content
    

class SeriesReviewForm(forms.ModelForm):
    class Meta:
        model = SeriesReview
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 11)]),
            'content': forms.Textarea(attrs={'rows': 5})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.series = kwargs.pop('series', None)
        super().__init__(*args, **kwargs)

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if self.instance.pk:
            # Exclude the current review from the validation check
            if SeriesReview.objects.filter(
                user=self.user, series=self.series, content=content
            ).exclude(pk=self.instance.pk).exists():
                raise ValidationError(
                    "You have already submitted a review with the same "
                    "content."
                )
        else:
            if SeriesReview.objects.filter(
                user=self.user, series=self.series, content=content
            ).exists():
                raise ValidationError(
                    "You have already submitted a review with the same "
                    "content."
                )
        return content


class MovieFilterForm(forms.Form):
    genre = forms.ModelChoiceField(queryset=Genre.objects.none(), required=False)
    min_rating = forms.IntegerField(min_value=1, max_value=10, required=False)
    release_year = forms.IntegerField(min_value=1900, max_value=2100, required=False)


class SeriesFilterForm(forms.Form):
    genre = forms.ModelChoiceField(queryset=Genre.objects.none(), required=False)
    first_air_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    last_air_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    number_of_seasons = forms.IntegerField(min_value=1, required=False)
