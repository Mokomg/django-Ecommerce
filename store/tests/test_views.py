from importlib import import_module

from django.conf import settings
# from django.contrib.auth.models import User
from account.models import UserBase as User
from django.http import HttpRequest
from django.test import (  # Client helps us simulate a web browser to test views
    Client, TestCase)
from django.urls import reverse

from store.models import Category, Product
from store.views import product_all

# @skip("demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        Category.objects.create(name="django", slug="django")
        User.objects.create(user_name="admin", email="admin@admin.com")
        self.data1 = Product.objects.create(category_id=1, created_by_id="1", title="Django Beginners",
                                            slug="django-beginners", price="19.99", image="django")

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get("/", HTTP_HOST="noaddress.com")
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST="localhost")
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_product_list_url(self):
        """
        Test category response status
        """
        response = self.c.get(
            reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product Response Status
        """
        response = self.c.get(reverse("store:product_detail", args=["django-beginners"]))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category Response Status
        """
        response = self.c.get(reverse("store:category_list", args=["django"]))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = product_all(request)  # sending a request directly to the actual view
        html = response.content.decode("utf8")
        self.assertIn("<title>BookStore</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)
