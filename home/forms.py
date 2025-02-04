from .models import MovieReview
from django import forms
from django.core.exceptions import ValidationError


class ReviewForm(forms.ModelForm):
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