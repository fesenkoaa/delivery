from django import forms
from .models import Comment


class ReviewsForm(forms.ModelForm):
    auth = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        label="Imię", required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
        label="email", required=True
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        label="Posłanie", required=True
    )

    class Meta:
        model = Comment
        fields = ('auth', 'email', 'message')