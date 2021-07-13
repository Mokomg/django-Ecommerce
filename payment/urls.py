from django.urls import path

from . import views

app_name = "payment"

urlpatterns = [
    path('', views.basketView, name="basket"),
    path("orderplaced/", views.order_placed, name="order_placed"),
    path("webhook", views.stripe_webhook), # stripe sends data to this url
]