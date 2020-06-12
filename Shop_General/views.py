from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


# Models
from Products.models import Products, Category

# Create your views here.
def home(request, pk=None):

    if pk:
        user = User.objects.get(pk=pk)
    
    else:
        user = request.user

    categories = Category.objects.all()

    context = {"user":user, "categories":categories}

    return render(request, "general_views/home.html", context)



def shop(request, c_slug):
    category = get_object_or_404(Category, category_slug=c_slug)
    products = Products.objects.filter(product_category=category).order_by("-time_released")


    context = {"products" : products}
    return render(request, "general_views/shop.html", context)


def spec_product(request, c_slug, p_slug):
    category = get_object_or_404(Category, category_slug=c_slug)
    
    spec_product = Products.objects.get(product_slug=p_slug) # Might have to change to filter or chnage the other thing to fitler
    # FIX FIX # FIX FIX # FIX FIX # FIX FIX
    related_products = Products.objects.filter(product_category = category) # maybe order by rating  

    context = {"spec_product" : spec_product, "related_products" : related_products,}

    return render(request, "general_views/product.html", context)



