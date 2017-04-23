from django.test import TestCase
from .models import Book, Course, Subject
from datetime import datetime

class BookTestCase(TestCase):
    def setup(self):
        subject = Subject.objects.create(name="Math")
        course = Course.objects.create(subject=subject, name="AP English Language and Composition", teacher="Jared Friebel")
        book = Book.objects.create(course=course, name="They Say I Say", condition="New", author="Test Author")
        return book
    def test_book_name(self):
        book = self.setup()
        self.assertEqual(book.name, "They Say I Say")
    def test_book_course(self):
        book = self.setup()
        self.assertEqual(book.course.subject.name, "Math")
        self.assertEqual(book.course.name, "AP English Language and Composition")
        self.assertEqual(book.course.teacher, "Jared Friebel")
        