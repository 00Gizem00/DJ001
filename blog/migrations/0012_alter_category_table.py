# Generated by Django 4.2.4 on 2023-09-04 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_category_slugs'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
    ]