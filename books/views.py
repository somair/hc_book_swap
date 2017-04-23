from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.http import HttpResponse
from books.models import Book, Subject
from books.forms import BookForm
from books.utils import compose_message

def index(request):
    book_list = Book.objects.filter(sold=False)
    subject_list = Subject.objects.all()
    condition_list = (conditions[0] for conditions in settings.CONDITION_CHOICES)
    paginator = Paginator(book_list, 10)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    context_dict = {'books': books,
        'conditions': condition_list,
        'subjects': subject_list,
    }
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
    if request.user==book.listed_by:
        if request.method == 'POST':
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                book = form.save(commit=False)
                book.save()
                return my_books(request)
        else:
            form = BookForm(instance=book)
    else:
        return index(request)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user==book.listed_by:
        book.delete()
    return index(request)

def contact_seller(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    buyer = request.user
    success = False
    if not buyer.is_anonymous():
        msg = compose_message(buyer, book)
        seller = book.listed_by
        send_mail("HC Book Swap Interest", msg,
          "HC Book Swap <%s>" % settings.DEFAULT_FROM_EMAIL, [seller.email])
        success = True
    context_dict = {'success': success}
    return render(request, 'books/contact_success.html', context_dict)