from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'w-full border rounded-lg p-3'
        })
    )
    class Meta():
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class ProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name',
            'phone',
            'location',
            'bio',
            'avatar'
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full border rounded p-3',
                'placeholder': 'Enter your full name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg p-3',
                'placeholder': 'Enter your phone number'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg p-3',
                'placeholder': 'Enter your location'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'w-full border rounded-lg p-3',
                'rows': '4',
                'placeholder': 'Tell us about your yourself'
            })
        }