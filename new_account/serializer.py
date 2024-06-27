from rest_framework import serializers
from new_account.models import Account, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'transaction_time', 'description']


class AccountSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)

    class Meta:
        model = Account
        fields = ['account_number', 'first_name', 'last_name', 'balance', 'account_type',
                  'transactions']

        transactions = serializers.StringRelatedField


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'pin', 'account_type']

    # account_number = serializers.CharField(max_length=10)
    # first_name = serializers.CharField(max_length=25)
    # last_name = serializers.CharField(max_length=25)
    # balance = serializers.DecimalField(max_digits=9, decimal_places=2)
    # account_type = serializers.CharField(max_length=11)
