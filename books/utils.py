from django.conf import settings

def check_isbn(isbn):
    return True

def compose_message(buyer, book):
    return "%s (%s) would like to buy your book %s which you listed for $%s on HC Book Swap." % (buyer.username, buyer.email, book.name, book.price)