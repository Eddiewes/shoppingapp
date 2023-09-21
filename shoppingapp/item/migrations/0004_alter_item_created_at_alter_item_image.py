# Generated by Django 4.2.5 on 2023-09-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_rename_is_solid_item_is_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
    ]
