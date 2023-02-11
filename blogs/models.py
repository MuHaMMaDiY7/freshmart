from django.db import models
from ckeditor.fields import RichTextField
from users.models import UserModel


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    main_image = models.ImageField(upload_to='blogs/')
    banner_image = models.ImageField(upload_to='blogs/')
    first_image = models.ImageField(upload_to='blogs/')
    second_image = models.ImageField(upload_to='blogs/')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
        ordering = ('-id', )


class CommentModel(models.Model):
    body = models.TextField()
    blog = models.ForeignKey(BlogModel, on_delete=models.RESTRICT, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

