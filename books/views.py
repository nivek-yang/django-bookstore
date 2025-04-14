from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, "books/index.html")

def new(req):
    return render(req, "books/new.html")