from django.contrib import admin
from books.models import Book, Subject, Course

admin.site.register(Book)
admin.site.register(Subject)
admin.site.register(Course)