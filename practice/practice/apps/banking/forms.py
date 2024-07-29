from django import forms
from .models import Account, Transaction, Loan, Client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'contact', 'account_number', 'residence', 'gender']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'contact': forms.TextInput(attrs={'class': 'form-control',  'required': True}),
            'account_number': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'residence': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'gender': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }

        error_messages = {
            'name': {'required': 'Please enter your full name'},
            'email': {'required': 'Please enter your email address'},
            'phone_number': {'required': 'Please enter your phone number'},
            'account_number': {'required': 'Please enter your account number'},
            'gender': {'required': 'Please select your gender'},
            'department': {'required': 'Please select your department'},  # Update error message
            'employee_status': {'required': 'Please select your status'},
        }

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['client', 'balance']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'amount', 'transaction_type']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['client', 'amount']
