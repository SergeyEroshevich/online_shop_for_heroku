# Generated by Django 4.0.5 on 2022-08-02 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_rating_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]