# Generated by Django 3.2.5 on 2021-08-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_item_set_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='set_sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6, null=True),
        ),
    ]