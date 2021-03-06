# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 20:55
from __future__ import unicode_literals

import books.utils
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=128)),
                ('condition', models.CharField(choices=[(b'New', b'New'), (b'Like New', b'Like New'), (b'Very Good', b'Very Good'), (b'Good', b'Good'), (b'Acceptable', b'Acceptable')], max_length=20)),
                ('description', models.TextField(default='No description.')),
                ('isbn', models.CharField(default='.', max_length=20, validators=[books.utils.check_isbn_length, books.utils.check_isbn_validity])),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('submitted', models.DateField(default=datetime.datetime.today)),
                ('thumbnail', models.ImageField(default='books/default/default_book_image.png', upload_to=books.utils.get_image_file_path)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('teacher', models.CharField(default='N/A', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Subject'),
        ),
        migrations.AddField(
            model_name='book',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Course'),
        ),
        migrations.AddField(
            model_name='book',
            name='listed_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
