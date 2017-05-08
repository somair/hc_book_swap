import django_filters
from django.conf import settings
from books.models import Book

class BookFilter(django_filters.FilterSet):
    isbn = django_filters.CharFilter(max_length=20, label='ISBN')
    condition = django_filters.MultipleChoiceFilter(choices=settings.CONDITION_CHOICES)
    
    class Meta:
        model = Book
        fields = {
            'price': ['range'],
            'name': ['contains'],
            'condition': ['exact'],
            'isbn': ['exact'],
            'author': ['contains']
        }
        exclude = ['course', 'thumbnail', 'description', 'listed_by', 'sold', 'submitted']
        strict = 'IGNORE'
