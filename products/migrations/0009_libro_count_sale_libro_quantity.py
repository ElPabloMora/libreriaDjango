# Generated by Django 5.0.3 on 2024-05-10 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='count_sale',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='libro',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
