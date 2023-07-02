from django.shortcuts import render
from .models import Book, Author

def bookstore(request):
    author_name = request.GET.get('author', '')
    books = Book.objects.all()

    if author_name:
        books = books.filter(author__name__icontains=author_name)

    return render(request, 'bookstore.html', {'books': books})
