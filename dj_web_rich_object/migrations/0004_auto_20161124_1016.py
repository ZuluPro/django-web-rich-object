# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_web_rich_object', '0003_auto_20161124_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webrichobject',
            name='base_url',
            field=models.URLField(max_length=500, verbose_name='Base URL'),
        ),
    ]
