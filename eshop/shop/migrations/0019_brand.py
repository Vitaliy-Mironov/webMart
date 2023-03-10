# Generated by Django 4.1.5 on 2023-01-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_alter_product_color_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Бренд')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Добавлен')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменён')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
    ]
