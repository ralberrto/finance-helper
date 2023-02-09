from rest_framework import serializers
from .models import Account


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "name",
            "holder",
            "currency",
        ]


class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "name",
            "holder",
            "currency",
            "locked",
            "comment",
        ]
