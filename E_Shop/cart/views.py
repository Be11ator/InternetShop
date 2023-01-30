from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.forms import AddToCarz
from shop.models import Women
from .cart import Cart
from .forms import CartAddProductForm



@require_POST
def cart_add(request, product_id):
    pk_t = {}
    cart = Cart(request)
    product = get_object_or_404(Women, pk=product_id)
    pk_t['pk_t'] = product_id
    form = AddToCarz(request.POST, pk_t)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, size=cd['size'], color=cd['color'], quantity=cd['quantity'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Women, pk=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/carz.html', {'cart': cart})
