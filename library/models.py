from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.
class Book(models.Model):
    name_book = models.CharField(max_length=150)
    book_id = models.PositiveIntegerField()
    auth = models.CharField(max_length=150)
    category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name_book) 

class Student(models.Model):
    name_stu = models.OneToOneField(User, on_delete=models.CASCADE)
    stu_id = models.CharField(max_length=10, blank=True)
    special = models.CharField(max_length=10)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return str(self.name_stu) 

def expiry():
    return datetime.today() + timedelta(days=14)


class IssuedBook(models.Model):
    student_id = models.CharField(max_length=15, blank=True) 
    IssuedBook_id = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)