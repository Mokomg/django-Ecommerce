import stripe as stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from basket.basket import Basket


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