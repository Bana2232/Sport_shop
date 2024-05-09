from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Item, Cart, CarouselItems
from .forms import CommentForm


def index_page(request):
    items_list = Item.objects.all()
    slides = CarouselItems.objects.all()

    paginator = Paginator(items_list, 6)
    page_number = request.GET.get("page", 1)

    try:
        items = paginator.page(page_number)

    except EmptyPage:
        items = paginator.page(1)

    except PageNotAnInteger:
        items = paginator.page(1)

    return render(request, "index.html",
                  {"items": items, "paginator": paginator,
                   "slides": slides})


def about(request):
    return render(request, "about.html")


def item_page(request, item_id):
    try:
        item = get_object_or_404(Item, id=item_id)

        return render(request, "item.html",
                      {"item": item, "images": item.images.all(),
                       "comments": item.comments.all()})

    except Http404:
        return render(request, "Страница не существует")


def item_comment(request, item_id):
    comment = None
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.save()

        return redirect("shop:item_detail", item_id)

    else:
        form = CommentForm()

        return render(request, "comment.html",
                      {"form": form, "item": item,
                       "comment": comment})


def cart(request):
    cart = Cart.objects.all()
    cart_price = sum(el.item.price for el in cart)

    return render(request, "cart.html",
                  {"cart": cart,
                   "cart_price": cart_price})


def add_item_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    try:
        card = get_object_or_404(Cart, item=item)
        card.number += 1
        card.save()

    except Http404:
        Cart(item=item).save()

    return redirect("shop:item_detail", item_id)


def remove_from_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    try:
        card = get_object_or_404(Cart, item=item)
        card.delete()

    except Http404:
        pass

    return redirect("shop:cart")
