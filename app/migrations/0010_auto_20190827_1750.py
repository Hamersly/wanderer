# Generated by Django 2.2.4 on 2019-08-27 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190827_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='rubrics',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Rubrics', verbose_name='Рубрика'),
        ),
    ]