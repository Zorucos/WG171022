# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-01 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apli', '0005_auto_20171201_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
