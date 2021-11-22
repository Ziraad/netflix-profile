from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from account.models import Profile
from market.models import Order, Product


def shopping_cart(request):
    try:
        user = request.user.customer
        print(user)
        orders = Order.objects.filter(customer=user)

        products = Product.objects.filter(orders__customer=user)
        print('orders: ', orders)

        context = {
            'user': user,
            'orders': orders,
            'products': products,
        }

        if request.method == 'POST':
            order = Order.objects.get(customer=user)
            order.presenter.add_point()
            order.delete()

        return render(request, 'market/shopping_cart.html', context=context)
    except Exception as e:
        context = {
            'error': str(e)
        }
        return render(request, 'market/shopping_cart.html', context=context)


@login_required
def shopping_cart_add_items(request, slug):
    presenter = get_object_or_404(Profile, random_url=slug)
    products = Product.objects.all()
    context = {
        'presenter': presenter,
        'products': products,
    }
    try:
        user = request.user.customer
        context['user'] = user

        if request.method == 'POST':
            get_product = request.POST.get('product')
            print('get_product: ', get_product)
            product = Product.objects.filter(name=get_product)
            if product.exists():
                product = Product.objects.get(name=get_product)
            print('product: ', product)
            order = Order.initiate(customer=user, presenter=presenter)
            print('order: ', order)
            order.add_product(product)
            order.save()
            print('order:', order)

        return render(request, 'market/shopping_cart_add_item.html', context=context)
    except Exception as e:
        context['error'] = str(e)
        return render(request, 'market/shopping_cart_add_item.html', context=context)
