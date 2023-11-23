from django.urls import path
from .views import CategoryListView, get_category_products

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('category/<str:slug>/', get_category_products, name='product')
]