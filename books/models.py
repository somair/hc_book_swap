from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from books.utils import get_image_file_path
#from imagekit.models import ImageSpecField
#from imagekit.processors import ResizeToFill
#https://github.com/matthewwithanm/django-imagekit << implement tomorrow in class
from datetime import datetime

class Subject(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name
    def get_courses(self):
        return self.course_set
        
class Course(models.Model):
    subject = models.ForeignKey(Subject)
    name = models.CharField(max_length=128)
    teacher = models.CharField(max_length=128, default="N/A")
    def __str__(self):
        return '%s taught by %s' % (self.name, self.teacher)
    def get_books(self):
        return self.book_set

class Book(models.Model):
    author = models.CharField(max_length=128)
    condition = models.CharField(max_length=20, choices=settings.CONDITION_CHOICES)
    course = models.ForeignKey(Course)
    description = models.TextField(default="No description.")
    isbn = models.CharField(max_length=20,default=".")
    listed_by = models.ForeignKey(User, default=1)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sold = models.BooleanField(default=False)
    submitted = models.DateField(default=datetime.today)
    thumbnail = models.ImageField(upload_to=get_image_file_path, default='books/thumbnails/default_book_image.png')
    def __str__(self):
        return 'Title: %s, Condition: %s, Price %s, ISBN %s' % (self.name, self.condition, self.price, self.isbn)