

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')  # Replace 'product_list' with the URL name of your product list view
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})
