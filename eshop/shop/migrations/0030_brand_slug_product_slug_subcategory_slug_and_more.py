# Generated by Django 4.1.5 on 2023-01-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_category_slug_alter_product_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.CharField(max_length=100, null=True, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=100, null=True, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.CharField(max_length=100, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=100, null=True, verbose_name='Ссылка'),
        ),
    ]
