from django.urls import path
from .views import AccountListAPIView


urlpatterns = [
    path("accounts/", AccountListAPIView.as_view(), name="accounts"),
]
