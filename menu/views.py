from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category, Product


class CategoryListView(ListView):
    model = Category
    template_name = "category.html"
    context_object_name = 'categories'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_products'] = Product.objects.all()
        return context


def get_category_products(request, slug):
    categories =Category.objects.filter(slug=slug)
    if not categories.exists():
        raise Http404("Category not found")

    descendants = categories[0].get_descendants(include_self=True)

    category_products = Product.objects.filter(category__in=descendants)

    context = {
        'category': categories[0],
        'category_products': category_products,
    }
    return render(request, 'product.html', context
    )



