# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.views.generic import ListView, DetailView, CreateView, View,UpdateView
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from .forms import SignUpForm, LoginForm, AuthorForm, BookForm
from .models import Author, Book
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.urls import reverse
from django.utils.decorators import method_decorator

# serilizerss
from rest_framework import generics
from .serializers import AuthorSerializer, BookSerializer, AuthorDetailSerializer, BookDetailSerializer

def Home(request):
    return render(request, 'Homepage.html')

@login_required(login_url='login_view')
def admin_home(request):
    return render(request, 'index.html')


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'
    paginate_by = 10
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Author.objects.filter(Q(author_name__icontains=query))
        return Author.objects.all()

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'

@method_decorator(login_required, name='dispatch')
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_form.html'
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('author-list')
    
class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_form.html'
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('author-list')

    
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 10
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(Q(book_name__icontains=query))
        return Book.objects.all()

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('book-list')

    
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('book-list')

class RegisterView(View):
    template_name = 'register.html'
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        return render(request, self.template_name, {'form': form})

class LoginView(AuthLoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.request.GET.get('next', '/'))
        else:
            form.add_error(None, 'Invalid login credentials.')
            return self.form_invalid(form)


class LogoutView(AuthLogoutView):
    next_page = '/author-list/'
    
# myapp/api_views.py
class AuthorAPIListView(generics.ListAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Author.objects.filter(Q(author_name__icontains=query))
        return Author.objects.all()

class AuthorAPIDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer

class BookAPIListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(Q(book_name__icontains=query))
        return Book.objects.all()

class BookAPIDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer



