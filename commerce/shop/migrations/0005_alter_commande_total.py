# Generated by Django 5.0.4 on 2024-05-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
