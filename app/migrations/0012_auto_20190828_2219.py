# Generated by Django 2.2.4 on 2019-08-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190828_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubrics',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Рубрика'),
        ),
        migrations.AlterField(
            model_name='tl',
            name='title',
            field=models.CharField(blank=True, max_length=10000, null=True, verbose_name='Заголовок'),
        ),
    ]