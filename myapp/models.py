from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    is_Author = models.BooleanField(default = False)
    is_Book = models.BooleanField(default = False)
    
# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author_profile')
    email = models.EmailField()
    action = models.CharField(max_length=50,choices=[('Edit', 'Edit'), ('View', 'View')], default='Edit')
    status = models.CharField(max_length=50,choices =[('Checking','checking'),('checked','checked')],default='Checking',)
    
    def __str__(self):
        return self.author_name

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    action = models.CharField(max_length=50, choices=[('Edit', 'Edit'), ('View', 'View')], default='Edit')
    status = models.CharField(max_length=50,choices =[('Checking','checking'),('checked','checked')],default='Checking')   
    def __str__(self):
        return self.book_name