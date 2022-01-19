from datetime import date
from typing import Optional

from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request, date_: Optional[date] = None):
    template = 'books/books_list.html'
    books = Book.objects.all()
    previous_date = None
    next_date = None
    if books and date_:
        dates = sorted({book.pub_date for book in books})
        books = [book for book in books if book.pub_date == date_]
        i = dates.index(date_)
        if i != 0:
            previous_date = dates[i - 1]
        if i < len(dates) - 1:
            next_date = dates[i + 1]
    context = {
        'books': books,
        'previous_date': previous_date,
        'next_date': next_date,
    }
    return render(request, template, context)
