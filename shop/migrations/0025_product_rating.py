# Generated by Django 4.0.5 on 2022-08-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_remove_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]