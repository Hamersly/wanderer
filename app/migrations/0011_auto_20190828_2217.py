# Generated by Django 2.2.4 on 2019-08-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190827_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubrics',
            name='title',
            field=models.CharField(max_length=10000, verbose_name='Рубрика'),
        ),
    ]
