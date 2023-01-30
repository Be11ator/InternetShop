from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from shop.utils import *

User._meta.get_field('email')._unique = True

CATEGORY = [
    (Accessories, 'Аксессуары'),
    (Bags, 'Рюкзаки'),
    (Hoodies_or_Sweatshirts, 'Толстовки или свитшоты'),
    (Jackets_or_Coats, 'Куртки или пальто'),
    (Polos, 'Поло'),
    (Shirts, 'Рубашки'),
    (Shoes, 'Обувь'),
    (Sweaters, 'Свитера'),
    (T_Shirts, 'Футблоки'),
    (Trousers_or_Jeans, 'Брюки или джинсы')
]


class SizeProduct(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")

    class Meta:
        verbose_name = 'Цвет продукта'
        verbose_name_plural = 'Цвет продукта'
        ordering = ['id']

    def __str__(self):
        return self.name


class ColorProduct(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")

    class Meta:
        verbose_name = 'Цвет продукта'
        verbose_name_plural = 'Цвет продукта'
        ordering = ['id']

    def __str__(self):
        return self.name


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Информация")
    photo = models.ImageField(upload_to="photo/%Y/%m/%d", verbose_name="Фото")
    price = models.FloatField(max_length=20, verbose_name="Цена")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    publish = models.BooleanField(default=True, verbose_name="Публикация")
    colors = models.ManyToManyField(ColorProduct)
    sizes = models.ManyToManyField(SizeProduct)

    brand = models.ForeignKey("Brand", on_delete=models.PROTECT, null=True, verbose_name="Брэнд")
    category = models.CharField(verbose_name="Категория", choices=CATEGORY, null=True, max_length=30)

    @classmethod
    def get_search_product(cls, request):
        return cls.objects.filter(title__contains=request)

    @classmethod
    def get_search_product_category(cls, request_title, request_category):
        return cls.objects.filter(title__contains=request_title).filter(category=request_category)

    @classmethod
    def get_qeryset_brand(cls, requset_title, request_brand_id):
        return cls.objects.filter(title__contains=requset_title).filter(brand_id__slug=request_brand_id)

    @classmethod
    def get_qeryset_brand_id(cls, request_brand_id):
        return cls.objects.filter(brand_id__slug=request_brand_id)

    @classmethod
    def get_qeryset_product_slug(cls, request_product_slug):
        return cls.objects.filter(slug=request_product_slug)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'
        ordering = ['time_create', 'title']

    def get_absolute_url(self):
        return reverse("product", kwargs={'product_name': self.slug})

    def __str__(self):
        return self.title




class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Брэнд")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("brand", kwargs={'brand_slug': self.slug})

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнд'
        ordering = ['id']


class Gender(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Гендэр")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def get_absolute_url(self):
        return reverse("gender", kwargs={'gender_name': self.name})

    class Meta:
        verbose_name = 'Гендэр'
        verbose_name_plural = 'Гендэр'
        ordering = ['id']


class SortProduct(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def get_absolute_url(self):
        return reverse("catalog_sort", kwargs={'sort_name': self.slug})

    class Meta:
        verbose_name = 'Сортировка'
        verbose_name_plural = 'Сортировка'
        ordering = ['id']


class Carz(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    color = models.CharField(max_length=255, verbose_name="Цвет")
    price = models.FloatField(max_length=20, verbose_name="Цена")
    size = models.CharField(max_length=20, verbose_name="Размер")

    def __str__(self):
        return self.title
