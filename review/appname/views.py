from .models import Review

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book)

    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})

from django.shortcuts import redirect
from .models import Review

def review_submit(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        content = request.POST.get('content')
        rating = request.POST.get('rating')

        book = get_object_or_404(Book, pk=book_id)
        review = Review(book=book, content=content, rating=rating)
        review.save()

    return redirect('book_detail', pk=book_id)
