# Generated by Django 4.1.5 on 2023-03-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0045_alter_order_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercontent',
            name='product_id',
            field=models.BigIntegerField(verbose_name='ID товара'),
        ),
    ]