# Generated by Django 5.0.8 on 2025-02-11 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_gallery_dish_alter_gallery_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='dish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.dish'),
        ),
    ]
