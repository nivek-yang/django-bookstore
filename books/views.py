from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# Create your views here.
def index(req):
    if req.POST:
        title = req.POST["title"]
        publisher = req.POST["publisher"]
        publication_date = req.POST["publication_date"]
        price = req.POST["price"]
        page = req.POST["page"]

        book = Book.objects.create(
            title=title,
            publisher=publisher,
            publication_date=publication_date,
            price=price,
            page=page
        )

        return redirect("books:show", book.id)

    else:
        books = Book.objects.all()
        return render(req, "books/index.html", {"books": books})

def new(req):
    return render(req, "books/new.html")

def show(req, id):
    book = get_object_or_404(Book, pk=id)
    return render(req, "books/show.html", {"book": book})