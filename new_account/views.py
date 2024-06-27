from decimal import Decimal
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account, Transaction
from .serializer import AccountCreateSerializer
from .serializer import AccountSerializer


# To combine related views into one instead of repeating codes for each clas
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer




# USING MIXINS
class ListAccount(ListCreateAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer

    # def get_queryset(self):
    #     return Account.objects.all()
    #
    # def get_serializer_class(self):
    #     return AccountCreateSerializer


# # 1. function based view
# class ListAccount(APIView):
#
#     def get(self, request):
#         accounts = Account.objects.all()
#         serializer = AccountSerializer(accounts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = AccountCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# 2. class based view
# @api_view(['GET', 'POST'])
# def list_account(request):
#     if request.method == 'GET':
#         account = Account.objects.all()
#         serializer = AccountSerializer(account, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = AccountCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class AccountDetail(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer

# # 1. function based view
# class AccountDetail(ListCreateAPIView):
#     def get(self, request, pk):
#         account = get_object_or_404(Account, pk=pk)
#         serializer = AccountCreateSerializer(account)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         account = get_object_or_404(Account, pk=pk)
#         serializer = AccountCreateSerializer(account, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         account = get_object_or_404(Account, pk=pk)
#         account.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# 2. class based view
# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def account_details(request, pk):
#     account = get_object_or_404(Account, pk=pk)
#     if request.method == 'GET':
#         serializer = AccountSerializer(account)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = AccountCreateSerializer(account, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         account.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def deposit(request):
    account_number = request.data['account_number']
    amount_deposited = request.data['amount']
    account = get_object_or_404(Account, pk=account_number)
    account.balance += Decimal(amount_deposited)
    account.save()
    Transaction.objects.create(
        account=account,
        amount=amount_deposited)
    return Response(data={"message": "Amount deposited successfully"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def withdrawal(request):
    account_number = request.data['account_number']
    amount = request.data['amount']
    pin = request.data['pin']
    account = get_object_or_404(Account, pk=account_number)
    if account.pin == pin:
        if account.balance > amount:
            account.balance -= Decimal(amount)
            account.save()
            Transaction.objects.create(
                account=account,
                amount=amount
            )
        else:
            return Response(data={"message": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={"message": "Invalid pin"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data={"message": "Amount withdrawn successfully"}, status=status.HTTP_200_OK)
