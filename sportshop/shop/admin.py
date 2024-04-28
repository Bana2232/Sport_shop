from django.contrib import admin
from .models import Item, Comment, Cart, Images


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "rating"]
    search_fields = ["title", "description"]
    list_filter = ["added"]
    date_hierarchy = "added"
    ordering = ["added"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["item", "is_selected", "number"]
    search_fields = ["item"]
    list_filter = ["is_selected", "number"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["item", "name", "email", "created", "updated", "active"]
    search_fields = ["item", "name", "email"]
    list_filter = ["item", "name", "created", "active"]
    date_hierarchy = "updated"
    ordering = ["created"]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    ...
