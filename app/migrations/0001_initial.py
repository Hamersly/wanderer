# Generated by Django 2.2.4 on 2019-08-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Главная страница',
            },
        ),
    ]