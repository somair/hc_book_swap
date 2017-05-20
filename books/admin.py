from django.contrib import admin
from books.models import Book, Subject, Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'teacher',)
    list_display_links = ('name',)
    search_fields = ('name', 'teacher',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('listed_by', 'name', 'author', 'isbn', 'submitted')
    list_display_links = ('name',)
    search_fields = ('name', 'author', 'isbn',)
    list_per_page = 20

admin.site.register(Book, BookAdmin)
admin.site.register(Subject)
admin.site.register(Course, CourseAdmin)