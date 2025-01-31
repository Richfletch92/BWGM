from .models import MovieReview
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 11)]),
            'content': forms.Textarea(attrs={'rows': 5})
        }
