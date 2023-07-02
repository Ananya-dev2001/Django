from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment
from .forms import CommentForm

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(post=blog)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
    else:
        form = CommentForm()
    
    return render(request, 'blog_detail.html', {'blog': blog, 'comments': comments, 'form': form})
