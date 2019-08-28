from django.db import models
from django.urls import reverse

# '''Модель главной страницы'''
class TL(models.Model):
    title = models.CharField(max_length=10000, null=True, blank=True, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

# '''Модель туристических маршрутов'''
class Rs(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    km = models.FloatField(null=True, blank=True,verbose_name='Расстояние')
    map = models.TextField(null=True, blank=True,verbose_name='Карта')
    content = models.TextField(null=True, blank=True,verbose_name='Описание')
    slug = models.SlugField(max_length=50,unique=True, verbose_name='URL')
    trek = models.FileField(upload_to='app/trek/', null=True, blank=True, verbose_name='Трек')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

# '''Рубрики статей'''
class Rubrics(models.Model):
    title = models.CharField(max_length=200, verbose_name='Рубрика')
    slug = models.SlugField(max_length=50,unique=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('rubrics_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'

# '''Сами статьи'''
class Outfit(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    rubrics = models.ForeignKey('Rubrics',null=True, verbose_name='Рубрика', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('outfit_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'