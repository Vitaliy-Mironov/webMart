# Generated by Django 4.1.5 on 2023-01-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_alter_brand_slug_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Размещ.на сайте'),
        ),
    ]
