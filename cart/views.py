from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from posts.models import Post

from .cart import Cart
from .forms import CartAddProductForm, OrderForm
from .models import Customer



@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Post, id=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Post, id=pk)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def get_checkout(request):
    cart = Cart(request)
    form = OrderForm(request.POST or None)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],'product': item['product'],'update': True})
    return render(request, 'cart/checkout.html', {
        'cart': cart,
        'form': form})


@transaction.atomic
def make_order(request):
    cart = Cart(request)
    form = OrderForm(request.POST or None)
    customer = Customer.objects.get(user=request.user)
    if form.is_valid():
        new_order = form.save(commit=False)
        new_order.customer = customer
        new_order.first_name = form.cleaned_data['first_name']
        new_order.last_name = form.cleaned_data['last_name']
        new_order.phone = form.cleaned_data['phone']
        new_order.address = form.cleaned_data['address']
        new_order.bying_type = form.cleaned_data['bying_type']
        new_order.order_date = form.cleaned_data['order_date']
        new_order.comment = form.cleaned_data['comment']
        new_order.in_cart = cart.get_cart()
        new_order.cart = cart.clear()
        new_order.save()
        customer.orders.add(new_order)
        messages.add_message(
            request,
            messages.INFO,
            'Спасибо за заказ! Менеджер с Вами свяжется')
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/checkout/')
