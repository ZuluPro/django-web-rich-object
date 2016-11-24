# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_web_rich_object', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webrichobject',
            name='url',
            field=models.URLField(max_length=500, verbose_name='URL'),
        ),
    ]
