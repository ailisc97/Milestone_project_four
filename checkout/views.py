from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JtcBvCx1dhRXL7wfnl133c2WZO31u9wFfkGiIYbQmOEeRHRiCokO094WyiMwSSMtpYm2cb6Ok14lPtHA4ngzHpd00wEKrSv15',
        'client_secret': 'sk_test_51JtcBvCx1dhRXL7weMHfetPLc3eEaBFY65YkmAVwvImeK17sDEf4ptqHz0cbod85JBFbnQ5YsbJ5O3FXobjC8knQ00RfuRIBTK',
    }

    return render(request, template, context)