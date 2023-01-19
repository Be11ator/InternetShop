# Generated by Django 4.1.2 on 2022-10-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_colorproduct_sizeproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
                ('price', models.FloatField(max_length=20, verbose_name='Цена')),
                ('size', models.FloatField(max_length=20, verbose_name='Размер')),
            ],
        ),
    ]
