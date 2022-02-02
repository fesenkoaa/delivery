from django import forms
from .models import Order

ORDER_TYPE = (
    ('odbiór osobisty (+prezent)', 'odbiór osobisty (+prezent)'),
    ('dowóz na adres (od 5zl.)', 'dowóz na adres (od 5zl.)')
)


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* imię'}),
        label="", required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* nazwisko'}),
        label="", required=True
    )
    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* telefon'}),
        label="", required=True
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        label="", required=False
    )
    order_type = forms.ChoiceField(
        choices=ORDER_TYPE,
        label="",
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ))
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'miasto'}),
        label="", required=False
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adres'}),
        label="", required=False
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'wiadomość: czas, kod do bramy, notatki'}),
        label="", required=False
    )

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'phone', 'email', 'order_type', 'city', 'address', 'message')
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* imię', 'label': None}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* nazwisko'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* telefon'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        #     'order_type': forms.Select(attrs={'class': 'form-control'}),
        #     'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'miasto'}),
        #     'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adres'}),
        #     'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'wiadomość'}),
        # }
