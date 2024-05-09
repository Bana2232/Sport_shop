from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Item, Cart, CarouselItems, Category
from .forms import CommentForm


def index_page(request):
    categories = Category.objects.all()
    filt = request.GET.get("filt", None)

    if filt:
        items_list = Item.objects.filter(category_id=filt)

    else:
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
                   "slides": slides, "categories": categories})


def about(request):
    return render(request, "about.html")


def item_page(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    comments = item.comments.all()

    paginator = Paginator(comments, 4)
    page_number = request.GET.get("page", 1)

    try:
        comments = paginator.page(page_number)

    except EmptyPage:
        comments = paginator.page(1)

    except PageNotAnInteger:
        comments = paginator.page(1)

    sum_rating = 0
    length = 0

    for comment in comments:
        length += 1
        sum_rating += comment.rate

    average = round(sum_rating / length, 2) if length != 0 else 0

    return render(request, "item.html",
                  {"item": item, "images": item.images.all(),
                   "comments": comments, "paginator": paginator,
                   "average": average})


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
