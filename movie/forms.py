from django.contrib.auth.forms import UserCreationForm
from .models import user
from django import forms

class HomeForm(forms.Form):
    email = forms.EmailField()

class CreateAcoountForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    
    class Meta:
        model = user
        fields = ('username', 'email', 'password1', 'password2')