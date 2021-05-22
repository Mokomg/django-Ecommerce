from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=255, db_index=True)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="product", verbose_name=_("Product"), on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE,
                                   related_name="product_creator")
    title = models.CharField(_("Title"), max_length=255)
    author = models.CharField(_("Author"), max_length=255, default="admin")
    description = models.TextField(_("Description"), blank=True)
    image = models.ImageField(_("Image"), upload_to="images", default="images/default.jpg",
                              height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(_("Slug"), max_length=255)
    price = models.DecimalField(_("Price"), max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(_("In Stock"), default=True)
    is_active = models.BooleanField(_("Active"), default=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = "Products"
        ordering = ("-created", "title")

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
