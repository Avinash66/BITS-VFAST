# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-06 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deluxeroom',
            name='dept',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='deluxeroom',
            name='student',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='normalroom',
            name='dept',
            field=models.CharField(default='', max_length=255),
        ),
    ]