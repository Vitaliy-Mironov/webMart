# Generated by Django 4.1.5 on 2023-01-09 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Цвет')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Добавлен')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменён')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвет',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.color', verbose_name='Цвет'),
        ),
    ]
