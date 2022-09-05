from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings



# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(to = settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null = True)
    reg_number = models.CharField(max_length=20, null=True, unique=True)
    course = models.CharField(max_length=30, null=True)
    college = models.CharField(max_length=80, null=True)
    total_books_due=models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
        # return self.reg_number or " "

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
    copies_available = models.IntegerField(blank=True, default=0)
    total_copies = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)


class Borrowed(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, null=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    issue_date = models.DateTimeField(null=True,blank=True)
    return_date = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.student.user.first_name + " borrowed " +self.book.title or''


    