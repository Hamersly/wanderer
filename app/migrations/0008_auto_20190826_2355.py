# Generated by Django 2.2.4 on 2019-08-26 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190826_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Рубрика')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name_plural': 'Рубрики',
                'verbose_name': 'Рубрика',
            },
        ),
        migrations.AlterField(
            model_name='rs',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='rs',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Контент')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('rubrics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Rubrics', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Статьи',
                'verbose_name': 'Статья',
            },
        ),
    ]
