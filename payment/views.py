import stripe as stripe

import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from basket.basket import Basket

from orders.views import payment_confirmation


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')


class Error(TemplateView):
    template_name = 'payment/error.html'

@login_required
def basketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price()) # stripe takes intents as int not decimal. so we have to convert
    total = total.replace('.', '')
    total = int(total)

    print("total"),

    stripe.api_key = "sk_test_51JCUg3KvELx4Sm5hfSomtogvUhgSZTH0bTL8AIO3tA3os8jQYXVxiDlJSD7ao07xiuwCLcZI2rIb4oCxaDTLI2DZ00KEgxP5bQ"
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='cad',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {"client_secret": intent.client_secret})


@csrf_exempt
def stripe_webhook(request):
    print("inside stripe webhook")
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        print("payment_intent.succeded")
        payment_confirmation(event.data.object.client_secret)

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)