from django.db import models

from apps.tags.models import Tag

class Post(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    image = models.ImageField(
        upload_to='posts/',
        verbose_name='Картинка',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    tag = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='posts'
    )


