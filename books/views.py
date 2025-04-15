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
        books = Book.objects.order_by("-id")
        return render(req, "books/index.html", {"books": books})

def new(req):
    return render(req, "books/new.html")

def show(req, id):
    book = get_object_or_404(Book, pk=id)
    return render(req, "books/show.html", {"book": book})

def update(req, id):
    if req.POST:
        book = get_object_or_404(Book, pk=id)

        book.title = req.POST["title"]
        book.publisher = req.POST["publisher"]
        book.publication_date = req.POST["publication_date"]
        book.price = req.POST["price"]
        book.page = req.POST["page"]

        book.save()
        return redirect("books:show", book.id)
    else:
        book = get_object_or_404(Book, pk=id)
        return render(req, "books/update.html", {"book": book})
    
def delete(req, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()

    return redirect("books:index")