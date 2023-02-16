# Generated by Django 4.1.5 on 2023-01-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_product_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='code_number',
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.PositiveBigIntegerField(help_text='Только цифры с кодом, например: 375291234567', verbose_name='Мобильный телефон (А1, МТС, life)'),
        ),
    ]
