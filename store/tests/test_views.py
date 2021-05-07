from unittest import skip # provides us the ability to skip test

from django.test import TestCase, Client # Client helps us simulate a web browser to test views
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products

# @skip("demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="admin")
        self.data1 = Product.objects.create(category_id=1, created_by_id="1", title="Django Beginners", slug="django-beginners", price="19.99", image="django")

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        reponse = self.c.get("/")
        self.assertEqual(reponse.status_code, 200)

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
        response = all_products(request) # sending a request directly to the actual view
        html = response.content.decode("utf8")
        # print(html)
        self.assertIn("<title>Home</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)