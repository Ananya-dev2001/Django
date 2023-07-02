from django.shortcuts import render
from django.http import JsonResponse
from .models import Account

def create_or_update_account(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        balance = request.POST.get('balance')
        account_type = request.POST.get('account_type')

        try:
            account = Account.objects.get(account_number=account_number)
            account.balance = balance
            account.account_type = account_type
            account.save()
            response = {'message': 'Account updated successfully.'}
        except Account.DoesNotExist:
            account = Account(account_number=account_number, balance=balance, account_type=account_type)
            account.save()
            response = {'message': 'Account created successfully.'}

        return JsonResponse(response)

    return render(request, 'create_account.html')
