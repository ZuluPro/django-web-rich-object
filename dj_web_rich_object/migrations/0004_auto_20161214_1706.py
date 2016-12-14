# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_web_rich_object', '0003_auto_20161124_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='webrichobject',
            name='author',
            field=models.CharField(max_length=100, null=True, verbose_name='author', blank=True),
        ),
        migrations.AddField(
            model_name='webrichobject',
            name='subtype',
            field=models.CharField(default='app', max_length=30, verbose_name='subtype'),
            preserve_default=False,
        ),
    ]
