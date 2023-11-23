from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField( max_length=50, unique=True, blank=True, null=True)
    parent = TreeForeignKey( 'self',  on_delete=models.CASCADE, null=True,  blank=True,  related_name='children', )
    slug = models.SlugField(max_length=150, null=True,)

    class MPTTMeta:
        order_insertion_by = ['name',]

    class Meta:
        unique_together = [['parent', 'slug',]]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('product', args=[str(self.slug)])

    def __str__(self):
        return f'{self.name}, {self.parent}'



class Product(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100, null=True, )
    description = models.TextField(verbose_name='description', null=True, )
    category = TreeForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT,
                              related_name='goods_to_category', )
    slug = models.SlugField(max_length=150, )
    image = models.ImageField(upload_to="uploads", null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}, {self.category}'
