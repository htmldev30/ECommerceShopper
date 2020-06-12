from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .models import Order, OrderItem
from Products.models import Products
from .gen_order_id import generate_order_id
from User.models import UserProfile
from django.contrib.auth.models import User
import datetime
# Create your views here.


def get_user_pending(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        #If order exists then we return
        return order[0]
    return 0


@login_required()
def my_cart(request):
    cart = get_user_pending(request)
    context = {
        'cart' : cart,
    }

    return render(request, 'user_cart/cart.html', context)

@login_required()
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    product = Products.objects.filter(id=kwargs.get('item_id', "")).first() #it assigns item_id to the specific id

    if product in user_profile.product.all():
        return HttpResponse("You already own this bruh")
    
    order_item, status = OrderItem.objects.get_or_create(product=product)
    
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        user_order.ref_key = generate_order_id()
        user_order.save()

    return redirect("/my_cart")

# Can also pass in kwargs
@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    return redirect("/my_cart")

'''@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending(request)
    context = {
        'order' : existing_order
    }

    return render(request, 'user_cart/cart.html', context)'''


'''@login_required
def checkout(request):
    existing_order = get_user_pending(request)
    context = {
        "order" : existing_order
    }

    return render(request, "user_cart/cart.html", context)'''


'''@login_required()
def process_payment(request, order_id):
    # processing payment

    return redirect("home")'''


@login_required()
def update_transaction_records(request, order_id):
    # get the order being processed
    order_to_purchase = Order.objects.filter(pk=order_id).first()

    # update placed order

    order_to_purchase.is_ordered = True
    order_to_purchase.date_ordered = datetime.datetime.now()
    order_to_purchase.save()

    #get all items in the order generates a query set
    order_items = order_to_purchase.items.all()

    #update order items
    order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())

    #add producs to user profile

    user_profile = get_object_or_404(UserProfile, user=request.user)

    #get the products from the items

    order_products = [item.product for item in order_items]
    # * allows you to add all the objects in the list order_products
    user_profile.product.add(*order_products)

    user_profile.save()
    return redirect("home")



    


