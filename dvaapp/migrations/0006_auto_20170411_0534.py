# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 05:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0005_auto_20170411_0449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vdnserver',
            old_name='token',
            new_name='last_token',
        ),
        migrations.RemoveField(
            model_name='vdnserver',
            name='username',
        ),
    ]
