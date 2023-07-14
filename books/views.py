from django.shortcuts import render, redirect
from .models import Books
# Create your views here.

def ebooks(request):
    if request.method == "POST" and request.FILES:
        book_title = request.POST["book_title"]
        book = request.FILES["add_file"]
        username = request.user.username
        if username == "":
            username = "Anonymous"
        upload_book = Books.objects.create(book_title = book_title, file = book, username = username)
        upload_book.save()
        return redirect("/ebooks")
    books = Books.objects.all().order_by("book_title")
    context = {
        "books": books
    }
    return render(request, "books/books.html", context)