# Generated by Django 2.2 on 2020-08-01 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
