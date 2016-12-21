# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_web_rich_object', '0005_auto_20161215_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='webrichobject',
            name='created_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='created time', blank=True),
        ),
        migrations.AddField(
            model_name='webrichobject',
            name='modified_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='modified time', blank=True),
        ),
        migrations.AddField(
            model_name='webrichobject',
            name='published_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='published time', blank=True),
        ),
    ]
