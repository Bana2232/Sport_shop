from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    price = models.IntegerField()
    rating = models.FloatField(default=0)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    def image_path(self, filename):
        return f"shop/static/product_images/{str(self.item.id)}/{filename}"

    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name="images")
    image = models.ImageField(upload_to=image_path)


class Cart(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name="cart")
    is_selected = models.BooleanField(default=True)
    number = models.IntegerField(default=1)


class Comment(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name="comments")

    name = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField()
    rate = models.IntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created"]
        indexes = [
            models.Index(fields=["created"])
        ]

    def __str__(self):
        return f"Комментарий пользователя {self.name} к {self.item}"
