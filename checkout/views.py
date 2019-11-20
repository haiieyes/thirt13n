import stripe
from django.conf import settings
from django.shortcuts import render, reverse, redirect
from cart.models import CartItem
from accounts.views import index

def calculate_cart_cost(request):
    all_cart_items = CartItem.objects.filter(owner=request.user)
    amount = 0
    for cart_item in all_cart_items:
        amount += cart_item.product.cost * cart_item.quantity
    return amount

# Create your views here.
def charge(request):
    if request.method == 'GET':
        amount = calculate_cart_cost(request)
        # key = settings.STRIPE_PUBLISHABLE_KEY
        key = "pk_test_OLhHq6JnkHlZvXQazkhDsivY00hy6csUbf"
        return render(request, 'checkout/checkout.template.html',{
            'key' : key,
            'amount' : amount
        })
    else:
        # stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.api_key = "sk_test_fqxcZAAaweRwMMiPnLNimL5c00g1JS7o0x"
        charge = stripe.Charge.create(
            amount=calculate_cart_cost(request),
            currency='SGD',
            description='Test Description',
            source=request.POST['stripeToken']
        )
        return redirect('index')