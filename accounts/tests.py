from django.test import TestCase
from django.urls import reverse
from .models import Account


class AccountTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.account = Account.objects.create(
            name="testname",
            holder="testholder",
            currency="anycurrency",
            locked=False,
            comment="somecomment",
        )

    def test_account_model(self):
        self.assertEqual(self.account.name, "testname")
        self.assertEqual(self.account.holder, "testholder")
        self.assertEqual(self.account.currency, "anycurrency")
        self.assertEqual(self.account.locked, False)
        self.assertEqual(self.account.comment, "somecomment")

    def test_resource_exist_in_location_list(self):
        response = self.client.get("/accounts/")
        self.assertEqual(response.status_code, 200)

    def test_resource_exist_in_location_details(self):
        response = self.client.get("/accounts/1/")
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        response = self.client.get(reverse("account_list"))
        self.assertEqual(response.status_code, 200)

    def test_details(self):
        response = self.client.get(
            reverse("account_details", kwargs={"id": self.account.id})
        )
        self.assertEqual(response.status_code, 200)
