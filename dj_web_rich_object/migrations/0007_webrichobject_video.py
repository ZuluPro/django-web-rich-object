# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_web_rich_object', '0006_auto_20161219_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='webrichobject',
            name='video',
            field=models.URLField(null=True, verbose_name='video', blank=True),
        ),
    ]
