from django.db import models


class ProductTagModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class ProductColorModel(models.Model):
    code = models.CharField(max_length=7)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductModel(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.TextField()
    long_description = models.TextField()
    price = models.FloatField()
    real_price = models.FloatField(default=0)
    discount = models.PositiveIntegerField(default=0)
    main_image = models.ImageField(upload_to='products/')
    tags = models.ManyToManyField(ProductTagModel, related_name='products')
    colors = models.ManyToManyField(ProductColorModel, related_name='products')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    # def real_price(self):
    #     if self.discount:
    #         return self.price - (self.price * self.discount) / 100
    #     return self.price

    def is_discount(self):
        return self.discount != 0

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-id',)

