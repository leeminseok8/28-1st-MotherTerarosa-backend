# Generated by Django 4.0 on 2021-12-28 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_urls',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='productstock',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='tastingnote',
            old_name='product_id',
            new_name='product',
        ),
    ]
