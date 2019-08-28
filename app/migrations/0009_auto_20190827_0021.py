# Generated by Django 2.2.4 on 2019-08-26 19:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190826_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='outfit',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Заголовок'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='outfit',
            name='rubrics',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Rubrics', verbose_name='Рубрика'),
        ),
    ]
