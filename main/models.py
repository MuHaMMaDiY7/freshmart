from django.db import models


class BannerModel(models.Model):
    image = models.ImageField(upload_to='banners/')
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
