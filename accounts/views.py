from django.shortcuts import render
from rest_framework import generics
from .models import Account
from .serializers import AccountListSerializer


class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer
