from django.urls import path
# This App
from . import views

app_name = "Cart"

urlpatterns = [
    path("add-to-cart/<item_id>", views.add_to_cart, name="add_to_cart"),
    path("item/delete/<item_id>", views.delete_from_cart, name="delete_from_cart"),
    path("update-transaction/<order_id>", views.update_transaction_records, name="update_record"),

]