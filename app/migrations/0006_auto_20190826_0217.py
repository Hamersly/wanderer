# Generated by Django 2.2.4 on 2019-08-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190826_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rs',
            name='trek',
            field=models.FileField(blank=True, null=True, upload_to='app/trek/', verbose_name='Трек'),
        ),
    ]
