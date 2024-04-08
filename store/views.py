from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def index(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    total_products = products.count()
    return render(request, "index.html", {"products": products, 'total_products': total_products,})

def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    total_products = products.count()
    return render(request, "products.html", {"products": products, 'total_products': total_products,})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=category.get_descendants(include_self=True)
    )
    total_products = products.count()
    return render(request, "category.html", {"category": category, "products": products, 'total_products': total_products,})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "product-detail.html", {"product": product})
