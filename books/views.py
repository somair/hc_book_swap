from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from books.models import Book
from books.forms import BookForm

def index(request):
    book_list = Book.objects.filter(sold=False)
    paginator = Paginator(book_list, 10)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    context_dict = {'books': books, 'conditions': settings.CONDITION_CHOICES}
    return render(request, 'books/listings.html', context_dict)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context_dict = {'book': book, 'is_anonymous': request.user.is_anonymous()}
    return render(request, 'books/detail.html', context_dict)
    
def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.listed_by = request.user
            book.save()
            return index(request)
        else:
            print(form.errors)
    return render(request, 'books/add_book.html', {'form': form})

def my_books(request):
    user = request.user
    if user.is_anonymous():
        return index(request)
    books = Book.objects.filter(listed_by=user)
    context_dict = {'books': books}
    return render(request, 'books/my_books.html', context_dict)

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST' and request.user is book.listed_by:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return my_books(request)
    else:
        return index(request)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user is book.listed_by:
        book.delete()
    return my_books(request)
