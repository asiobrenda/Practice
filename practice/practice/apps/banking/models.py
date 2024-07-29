from django.db import models
from django.conf import settings


class Client(models.Model):
    class Meta:
        verbose_name_plural = 'RegisterClient'
        ordering = ['id']

    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=30)
    account_number = models.CharField(max_length=50)
    residence = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class Account(models.Model):
    class Meta:
        verbose_name_plural = 'Account'

    client = models.OneToOneField(Client, on_delete=models.CASCADE, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.client

class Transaction(models.Model):
    class Meta:
        verbose_name_plural = 'Transaction'

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
        ('buy_shares', 'Buy Shares'),
        ('loan_payment', 'Loan Payment'),
    ]
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)

    def __str__(self):
        return self.account


class Loan(models.Model):
    class Meta:
        verbose_name_plural = 'Loan'

    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client + self.amount

