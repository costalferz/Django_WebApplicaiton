# Generated by Django 3.1.7 on 2021-05-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
