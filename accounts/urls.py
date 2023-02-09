from django.urls import path
from . import views


urlpatterns = [
    path("accounts/", views.AccountListAPIView.as_view(), name="account_list"),
    path(
        "accounts/<int:id>/",
        views.AccountDetailsAPIView.as_view(),
        name="account_details",
    ),
    path(
        "accounts/create/", views.AccountCreateAPIView.as_view(), name="account_create"
    ),
    path(
        "accounts/update/<int:id>",
        views.AccountRetrieveUpdateAPIView.as_view(),
        name="account_update",
    ),
]
