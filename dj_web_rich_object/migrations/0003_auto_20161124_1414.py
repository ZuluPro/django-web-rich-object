# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_web_rich_object', '0002_auto_20161124_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webrichobject',
            name='base_url',
            field=models.TextField(max_length=500, verbose_name='Base URL'),
        ),
        migrations.AlterField(
            model_name='webrichobject',
            name='site_name',
            field=models.CharField(max_length=200, null=True, verbose_name='site name', blank=True),
        ),
        migrations.AlterField(
            model_name='webrichobject',
            name='url',
            field=models.TextField(max_length=500, verbose_name='URL'),
        ),
    ]
