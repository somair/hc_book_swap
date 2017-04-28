from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import uuid
import os

# Helper functions for dealing with models

# Verify that the ISBN number is either 10 or 13 characters long
def check_isbn_length(isbn):
    if len(isbn) != 10 and len(isbn) != 13:
        raise ValidationError(
            _('%(isbn)s is not a valid ISBN - wrong length'),
            params={'isbn': isbn},
        )
# Verify that the last digit of the ISBN is valid
# On ISBN validity: http://www-math.ucdenver.edu/~wcherowi/jcorner/isbn.html
def check_isbn_validity(isbn):
    digits = list(isbn)
    for i, val in enumerate(digits):
        digits[i] = int(val)
    sum = 0
    if len(isbn)==10:
        for i in range(0,9):
            sum += ((i+1)*digits[i])
        if(digits[9] != sum % 11):
            raise ValidationError(
                _('%(isbn)s is not a valid ISBN-10 - wrong check digit'),
                params={'isbn': isbn},
            )
    elif len(isbn)==13:
        for i in range(0,12):
            if i%2==0:
               sum += digits[i]
            else:
                sum += (3*digits[i])
        if(digits[12] != 10 - (sum % 10)):
            raise ValidationError(
                _('%(isbn)s is not a valid ISBN-13 - wrong check digit'),
                params={'isbn': isbn},
            )
    
def get_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('books/thumbnails', filename)
    
# Helper functions for dealing with views

def compose_message(buyer, book):
    return "%s (%s) would like to buy your book %s (ID: %s) which you listed for $%s on HC Book Swap." % (buyer.username, buyer.email, book.name, book.id, book.price)