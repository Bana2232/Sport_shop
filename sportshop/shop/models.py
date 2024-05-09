from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"
        ordering = ["id"]

    category = models.CharField(max_length=50, verbose_name="Категория")

    def __str__(self):
        return self.category


class Item(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(max_length=4000, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    rating = models.FloatField(default=0, verbose_name="Рейтинг")
    added = models.DateTimeField(auto_now_add=True, verbose_name="Добавлен")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="items_by_category",
                                 verbose_name="Категория", null=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"

    def image_path(self, filename):
        return f"shop/static/product_images/{str(self.item.id)}/{filename}"

    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name="images", verbose_name="Товар")
    image = models.ImageField(upload_to=image_path, verbose_name="Изображение")


class Cart(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Корзина"

    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name="cart",
                             verbose_name="Товар")

    is_selected = models.BooleanField(default=True, verbose_name="Выбран")
    number = models.IntegerField(default=1, verbose_name="Количество")


class Comment(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name="comments",
                             verbose_name="Товар")

    name = models.CharField(max_length=25, verbose_name="Имя пользователя")
    email = models.EmailField(verbose_name="Электронная почта")
    body = models.TextField(verbose_name="Текст комментария")
    rate = models.IntegerField(default=1, verbose_name="Оценка")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлён")
    active = models.BooleanField(default=True, verbose_name="Опубликован")

    class Meta:
        ordering = ["created"]
        indexes = [
            models.Index(fields=["created"])
        ]

        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Комментарий пользователя {self.name} к {self.item}"


class CarouselItems(models.Model):
    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

    def image_path(self, filename):
        return f"shop/static/CarouselItems/{filename}"

    def __str__(self):
        return self.title

    image = models.ImageField(upload_to=image_path, verbose_name="Изображение")
    title = models.CharField(max_length=60, verbose_name="Заголовок", null=True)
    description = models.CharField(max_length=300, verbose_name="Описание", null=True)
