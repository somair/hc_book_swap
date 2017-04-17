from django import forms
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth.models import User

from books.models import Book, Course
from captcha.fields import ReCaptchaField

class BookForm(forms.ModelForm):
    author = forms.CharField(max_length=128, help_text="Author")
    captcha = ReCaptchaField()
    condition = forms.ChoiceField(help_text="Condition", choices=settings.CONDITION_CHOICES)
    course = forms.ModelChoiceField(queryset=Course.objects.order_by('-name'), help_text="Class/Course")
    name = forms.CharField(max_length=200, help_text="Title")
    description = forms.CharField(widget=forms.Textarea, help_text="Add any additional details you would like to provide.")
    isbn = forms.CharField(initial=0, help_text="ISBN")
    price = forms.IntegerField(initial=0, help_text="Price")
    sold = forms.BooleanField(initial=False, help_text="Has the book been sold? Leave the box unchecked if the book is available.", required=False)
    thumbnail = forms.ImageField(help_text="Please submit an image of the book.", required=False)
    
    class Meta:
        model = Book
        fields = ('name', 'author', 'condition', 'course', 'description', 'isbn', 'price', 'sold', 'thumbnail',)
        exclude = ('listed_by','submitted')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        isbn = cleaned_data.get('isbn')
        cleaned_isbn = ''
        for char in isbn:
            if char!='-':
                cleaned_isbn+=char
        cleaned_data['isbn'] = cleaned_isbn
        return cleaned_data