# Generated by Django 2.2.8 on 2021-09-02 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_login', '0002_category_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='p',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='p',
            new_name='user',
        ),
    ]
