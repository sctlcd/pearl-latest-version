from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


# Bag views

def view_bag(request):
    """
        A view that renders the bag contents page
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
        Add a quantity of the specified product to the shopping bag
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag

    context = {
        'product': product,
        'quantity': bag[item_id],
    }
    # reload product_detail page quantity updated accordingly to the quantity
    # in the shopping bag and reset quantity input number to 1
    return render(request, 'products/product_detail.html', context)


def adjust_bag(request, item_id):
    """
        Adjust the quantity of the specified product to the specified amount
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
        Remove the item from the shopping bag
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def item_detail(request, item_id, quantity):
    """
        A view to show individual product details
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(quantity)

    context = {
        'product': product,
        'quantity': quantity,
    }

    return render(request, 'products/product_detail.html', context)
