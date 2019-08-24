from django.db import models


# '''Модель главной страницы'''
class TL(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'