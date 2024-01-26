from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=30,
        label='',
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        widget=forms.TextInput(attrs={'class': 'vocab_register__form-input',
                                      'placeholder': 'Name'}
                               ),
    )

    email = forms.CharField(
        max_length=30,
        label='',
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        widget=forms.EmailInput(attrs={'class': 'vocab_register__form-input',
                                       'placeholder': 'Email'}
                                ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'vocab_register__form-input',
                                          'placeholder': 'Password'}),
        label='',
        min_length=3,
        help_text='Your custom help text for the password field.'
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        label='',
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        widget=forms.TextInput(attrs={'class': 'vocab_register__form-input',
                                      'placeholder': 'Name'}
                               ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'vocab_register__form-input',
                                          'placeholder': 'Password'}),
        label='',
        min_length=3,
        help_text='Your custom help text for the password field.'
    )

    class Meta:
        model = User
        fields = ["username", "password"]

