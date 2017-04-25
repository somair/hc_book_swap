from django.conf import settings
import uuid
import os

def check_isbn(isbn):
    return True
    
def get_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('books/thumbnails', filename)

def compose_message(buyer, book):
    return "%s (%s) would like to buy your book %s which you listed for $%s on HC Book Swap." % (buyer.username, buyer.email, book.name, book.price)