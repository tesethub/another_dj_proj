# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-18 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_auto_20160818_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Адрес для регистации через имейл'),
        ),
    ]