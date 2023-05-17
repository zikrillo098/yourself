from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тематика')


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(max_length=1000, verbose_name='Описание')
    watched = models.IntegerField(default=0, verbose_name='Просмотры')
    published = models.DateTimeField(auto_now=True)
    theme = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Темка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видосы'
        ordering = ['watched', 'theme']


class Gallery(models.Model):
    photo = models.ImageField(upload_to='photos/', verbose_name='Видео')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
