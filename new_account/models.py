from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.conf import settings
from .utility import generate_account_number
from .validators import validate_pin


class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    account_number = models.CharField(max_length=10,
                                      default=generate_account_number,
                                      unique=True, primary_key=True)
    pin = models.CharField(max_length=4, validators=[validate_pin], default='0000')
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    ACCOUNT_TYPE = [
        ('SAVINGS', 'Savings'),
        ('CURRENT', 'Current'),
        ('DOMICILIARY', 'Domiciliary'),
    ]
    account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=11, default='SAVINGS')

    def __str__(self):
        return f"{self.account_type} {self.balance}"


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('CREDIT', 'Credit'),
        ('DEBIT', 'Debit'),
        ('TRANSFER', 'Transfer')
    ]
    TRANSACTION_STATUS = [
        ('SUCCESSFUL', 'Successful'),
        ('PENDING', 'Pending'),
        ('FAILED', 'Failed'),
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10,
                                        choices=TRANSACTION_TYPE,
                                        default='CREDIT')
    transaction_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    Transaction_status = models.CharField(max_length=10,
                                          choices=TRANSACTION_STATUS,
                                          default='SUCCESSFUL')
