# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-13 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20160813_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='mfacode',
            name='tries_counter',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]