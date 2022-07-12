from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.

class User(AbstractUser):
    is_librarian = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

class Student(models.Model):
    pass

status = (
    ('Available', 'Available'),
    ('Reserved', 'Reserved'),
    ('Borrowed', 'Borrowed'),
)
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=10, null="True")
    book_edition = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    book_id = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='lib/covers/', null= False)
    status = models.CharField(default='Available', choices = status, max_length=20)
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)


class Borrowed(models.Model):
    pass

    