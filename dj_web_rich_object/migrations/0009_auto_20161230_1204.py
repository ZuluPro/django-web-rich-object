# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_web_rich_object', '0008_auto_20161229_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webrichobject',
            name='image',
            field=models.TextField(null=True, verbose_name='image', blank=True),
        ),
        migrations.AlterField(
            model_name='webrichobject',
            name='video',
            field=models.TextField(null=True, verbose_name='video', blank=True),
        ),
    ]
