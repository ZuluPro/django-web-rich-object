# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_web_rich_object', '0007_webrichobject_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='webrichobject',
            name='video_height',
            field=models.PositiveIntegerField(null=True, verbose_name='video height', blank=True),
        ),
        migrations.AddField(
            model_name='webrichobject',
            name='video_width',
            field=models.PositiveIntegerField(null=True, verbose_name='video width', blank=True),
        ),
    ]
