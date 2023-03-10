# Generated by Django 4.1.5 on 2023-01-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_brand_slug_product_slug_subcategory_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Ссылка'),
        ),
    ]
