from django.shortcuts import render
from django.http.response import JsonResponse

from basket.basket import Basket
from .models import Order, OrderItem

def add(request):
    print("in orders add view")
    basket = Basket(request)
    if request.POST.get("action") == "POST":
        user_id = request.user.id
        order_key = request.POST.get("order_key")
        basket_total = basket.get_total_price()

#         Check if the order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, full_name="John Doe", address1="address1",
                                         address2="address2", total_paid=basket_total, order_key=order_key) # replace static data with form data

            order_id = order.pk
            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item["product"], price=item["price"], quantity=item["qty"])

        response = JsonResponse({"success": "Return Something"})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders