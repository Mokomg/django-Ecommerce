from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    print(product.product_image.all())
    return render(request, "store/single.html", {"product": product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {"category": category, "products": products})
