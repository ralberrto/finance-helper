from django.shortcuts import render
from rest_framework import generics
from .models import Account
from .serializers import AccountListSerializer, AccountDetailsSerializer


class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer


class AccountDetailsAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Account.objects.all()
    serializer_class = AccountDetailsSerializer


class AccountCreateAPIView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailsSerializer


class AccountRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Account.objects.all()
    serializer_class = AccountDetailsSerializer
