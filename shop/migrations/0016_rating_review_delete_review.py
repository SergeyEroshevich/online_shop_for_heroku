# Generated by Django 4.0.5 on 2022-08-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_review_product_alter_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Отзыв'),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]