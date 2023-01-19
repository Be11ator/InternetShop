# Generated by Django 4.1.2 on 2022-10-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_carz'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='carz',
            name='size',
            field=models.CharField(max_length=20, verbose_name='Размер'),
        ),
    ]
