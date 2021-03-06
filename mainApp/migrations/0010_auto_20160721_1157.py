# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='images',
            field=models.ManyToManyField(blank=True, default=None, to='mainApp.Images', verbose_name='Картинки'),
        ),
        migrations.AddField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(blank=True, default=None, to='mainApp.Images', verbose_name='Картинки'),
        ),
        migrations.AlterField(
            model_name='place',
            name='adress',
            field=models.TextField(max_length=255, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='place',
            name='email',
            field=models.ManyToManyField(blank=True, default=None, to='mainApp.Emails'),
        ),
        migrations.AddField(
            model_name='place',
            name='site',
            field=models.ManyToManyField(blank=True, default=None, to='mainApp.Links'),
        ),
    ]
