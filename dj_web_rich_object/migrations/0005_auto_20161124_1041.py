# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_web_rich_object', '0004_auto_20161124_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webrichobject',
            name='base_url',
            field=models.TextField(max_length=500, verbose_name='Base URL'),
        ),
        migrations.AlterField(
            model_name='webrichobject',
            name='url',
            field=models.TextField(max_length=500, verbose_name='URL'),
        ),
    ]
