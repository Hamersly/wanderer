from django.db import models
from django.utils.text import slugify
from time import time

# '''Модель главной страницы'''
class TL(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

# '''Модель туристических маршрутов'''
def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Rs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    km = models.FloatField(null=True, blank=True,verbose_name='Расстояние')
    map = models.TextField(null=True, blank=True,verbose_name='Карта')
    content = models.TextField(null=True, blank=True,verbose_name='Описание')
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    trek = models.FileField(upload_to='app/trek/', null=True, blank=True, verbose_name='Трек')



    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'