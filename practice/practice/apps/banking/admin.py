from django.contrib import admin
from .models import Client, Account, Transaction, Loan

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact', 'account_number',  'residence', 'gender']
    list_filter = ['gender', 'residence']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['client', 'balance']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'transaction_type']


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['client', 'amount']