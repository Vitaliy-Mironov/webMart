# Generated by Django 4.1.5 on 2023-01-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_rename_second_name_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='Ссылка'),
        ),
    ]
