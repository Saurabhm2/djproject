# Generated by Django 5.0.7 on 2024-07-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prices',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sub_category',
            new_name='subcategory',
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]
