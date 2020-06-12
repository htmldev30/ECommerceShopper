from django.urls import path
# This App
from . import views

# Other Apps
from User import views as user_views
from Cart import views as cart_views

app_name = "Shop_General"

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", user_views.profile, name="profile"),
    path("create_profile", user_views.new_user, name="create_profile"),
    path("my_cart/", cart_views.my_cart, name="my_cart"),
    # Shop
    path("<slug:c_slug>/", views.shop, name="shop"),
    path("<slug:c_slug>/<slug:p_slug>", views.spec_product, name="product"),

]