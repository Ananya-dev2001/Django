from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm

def customer_view(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')

    customers = Customer.objects.all()

    account_type_filter = request.GET.get('account_type')
    account_number_filter = request.GET.get('account_number')

    if account_type_filter:
        customers = customers.filter(accounts__account_type=account_type_filter)

    if account_number_filter:
        customers = customers.filter(accounts__account_number__icontains=account_number_filter)

    context = {
        'form': form,
        'customers': customers,
    }

    return render(request, 'customer.html', context)
