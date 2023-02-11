from django.db import models


class ContactMessageModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    theme = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class BannerModel(models.Model):
    image = models.ImageField(upload_to='banners/')
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
