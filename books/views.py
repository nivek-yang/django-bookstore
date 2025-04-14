from django.shortcuts import render
from .models import Book

# Create your views here.
def index(req):
    books = Book.objects.all()
    return render(req, "books/index.html", {"books": books})

def new(req):
    return render(req, "books/new.html")