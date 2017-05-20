from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from books.utils import get_image_file_path, check_isbn_length, check_isbn_validity
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
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
    isbn = models.CharField(max_length=20, default=".", validators=[check_isbn_length, check_isbn_validity])
    listed_by = models.ForeignKey(User, default=1)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    submitted = models.DateField(default=datetime.today)
    thumbnail = models.ImageField(upload_to=get_image_file_path)
    square_thumbnail = ImageSpecField(source='thumbnail',
                                      processors=[Thumbnail(370,370)],
                                      format='JPEG',
                                      options={'quality': 60})

    def __str__(self):
        return 'Title: %s, Condition: %s, Price %s, ISBN %s' % (self.name, self.condition, self.price, self.isbn)