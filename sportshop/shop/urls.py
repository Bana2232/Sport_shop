from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.index_page, name="index"),
    path("about/", views.about, name="about"),
    path("<int:item_id>/", views.item_page, name="item_detail"),
    path("cart/", views.cart, name="cart"),
    path("<int:item_id>/add_comment/", views.item_comment, name="add_comment"),
    path("<int:item_id>/add_to_cart/", views.add_item_to_cart, name="cart_add"),
    path("<int:item_id>/remove_from_cart/", views.remove_from_cart, name="cart_remove"),
]
