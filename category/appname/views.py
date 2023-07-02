from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import CategoryForm

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    
    return render(request, 'create_category.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
