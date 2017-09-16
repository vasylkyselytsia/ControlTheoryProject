# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-16 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='category_photos')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(null=True, upload_to='product_photos')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='db.Category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
