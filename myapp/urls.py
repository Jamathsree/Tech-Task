# myapp/urls.py

from django.urls import path
from .views import (
    Home,admin_home,
    AuthorListView, AuthorDetailView, AuthorCreateView,AuthorUpdateView,
    BookListView, BookDetailView, BookCreateView,BookUpdateView,
    AuthorAPIListView, AuthorAPIDetailView, BookAPIListView, BookAPIDetailView,
    RegisterView, LoginView, LogoutView
)

urlpatterns = [
    path('', Home, name='Home'),
    path('admin_home', admin_home, name='admin_home'),

    # Views for web interface
    path('author-list/', AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('author-create/', AuthorCreateView.as_view(), name='author-create'),
    path('author/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author-edit'),
    
    path('book-list/', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book-create/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout_view'),


    # API URLs
    path('api/authors/', AuthorAPIListView.as_view(), name='author-api-list'),
    path('api/authors/<int:pk>/', AuthorAPIDetailView.as_view(), name='author-api-detail'),
    path('api/books/', BookAPIListView.as_view(), name='book-api-list'),
    path('api/books/<int:pk>/', BookAPIDetailView.as_view(), name='book-api-detail'),
]
