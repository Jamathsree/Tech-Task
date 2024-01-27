from django import forms
from .models import Author, Book,User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = get_user_model()  # Use get_user_model to get the custom user model
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        User = get_user_model()  # Use get_user_model to get the custom user model
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('This username is already taken. Please choose a different one.')
        return username
        
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_name', 'email', 'action', 'status']
       
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'author', 'action', 'status']
