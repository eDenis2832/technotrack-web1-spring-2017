# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='rate',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]