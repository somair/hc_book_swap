# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-13 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20170413_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(default=b'/static/images/default_book_image.png', upload_to='books/thumbnails'),
        ),
    ]
