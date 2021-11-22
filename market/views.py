from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from account.models import Profile
from market.models import Order, Product


def shopping_cart(request):
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
    return render(request, 'market/shopping_cart.html', context=context)


@login_required
def shopping_cart_add_items(request, str):
    user = request.user.customer
    print('user: ', user)
    presenter = get_object_or_404(Profile, random_url=str)
    products = Product.objects.all()

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

        # presenter.add_point()
        # return redirect('account:user_profile')

    context = {
        'user': user,
        'presenter': presenter,
        'products': products,
    }

    return render(request, 'market/shopping_cart_add_item.html', context=context)