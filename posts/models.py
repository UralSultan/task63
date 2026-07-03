from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    image = models.ImageField(upload_to='posts/', verbose_name='Картинка')
    description = models.TextField(blank=True, verbose_name='Описание')
    likes_count = models.PositiveIntegerField(default=0, verbose_name='Количество лайков')
    comments_count = models.PositiveIntegerField(default=0, verbose_name='Количество комментариев')
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True, verbose_name='Лайкнули')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at']

    def __str__(self):
        return f'Публикация {self.author}'
