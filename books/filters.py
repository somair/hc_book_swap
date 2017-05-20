import django_filters
from django.conf import settings
from books.models import Book
from django import forms

class BookFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter(required=False)
    isbn = django_filters.CharFilter(max_length=20, label='ISBN', required=False, lookup_expr='iexact')
    condition = django_filters.MultipleChoiceFilter(choices=settings.CONDITION_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    name = django_filters.CharFilter(max_length=120, lookup_expr='icontains', required=False)
    author = django_filters.CharFilter(max_length=120, lookup_expr='icontains', required=False)
    
    class Meta:
        model = Book
        fields = ['name', 'price', 'condition', 'isbn', 'author']
        exclude = ['course', 'thumbnail', 'description', 'listed_by', 'submitted']
        strict = 'IGNORE'
