from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book/(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^book/(?P<book_id>[0-9]+)/edit$', views.edit_book, name='edit_book'),
    url(r'^book/(?P<book_id>[0-9]+)/delete', views.delete_book, name='delete_book'),
    url(r'^book/(?P<book_id>[0-9]+)/contact', views.contact_seller, name='contact_seller'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^my_books/$', views.my_books, name='my_books'),
]