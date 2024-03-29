from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from eshop.settings import UNAUTHORIZED_USER_ID
from shop.models import Product, Order, OrderContent
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponseRedirect


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    # Возврат на страницу, вызвавшую функцию
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_datail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'update': True, })
    data = {
        'title': 'Корзина',
        'description': 'Корзина покупателя',
        'h1': 'Корзина покупателя',
        'bread': 'Корзина',
    }
    return render(request, 'cart/detail.html', context=data)


def cart_save(request):
    """_
    Сохранение заказа в БД
    """
    cart = Cart(request)
    if request.user.is_authenticated:
        id = request.user.id
    else:
        id = UNAUTHORIZED_USER_ID
    order = Order.objects.create(
        customer_id=id,
        total_value=cart.get_total_price(),
        is_paid=True
    )
    for item in cart:
        prod_id = item['product'].id,
        price = item['price'],
        quantity = item['quantity'],
        total_value = item['total_price'],
        order_content = OrderContent(
            product_id=prod_id[0],
            product_price=price[0],
            product_quantity=quantity[0],
            product_total_value=total_value[0],
            order=order
        )
        order_content.save()
    return redirect('cart:cart_sale')


def cart_sale(request):
    """
    Списание проданного товара с остатков в таблице Product
    """
    cart = Cart(request)
    for item in cart:
        product = get_object_or_404(Product, id=item['product'].id)
        remainder = product.balance - item['quantity']
        product.balance = remainder
        product.save(update_fields=["balance"])
        cart.remove(product)
    return redirect('shop:complete')
