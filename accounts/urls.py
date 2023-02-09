from django.urls import path
from .views import AccountListAPIView, AccountDetailsAPIView, AccountCreateAPIView


urlpatterns = [
    path("accounts/", AccountListAPIView.as_view(), name="account_list"),
    path("accounts/<int:id>/", AccountDetailsAPIView.as_view(), name="account_details"),
    path("accounts/create/", AccountCreateAPIView.as_view(), name="account_create"),
]
