# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-05 17:40
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20171028_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='short_name',
            field=models.CharField(max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='photo',
            field=models.ImageField(default='ingredient_photos/not_found_404.png', null=True, storage=django.core.files.storage.FileSystemStorage(location='E:\\Study\\4_Course(1)\\ControlTheory\\Project\\Project\\static'), upload_to='ingredient_photos'),
        ),
        migrations.AlterField(
            model_name='productingredients',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_ingredients', to='db.Product'),
        ),
    ]