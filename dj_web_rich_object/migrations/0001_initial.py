# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebRichObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('type', models.CharField(max_length=30, verbose_name='type')),
                ('image', models.URLField(null=True, verbose_name='image', blank=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('base_url', models.URLField(unique=True, verbose_name='Base URL')),
                ('site_name', models.CharField(max_length=100, null=True, verbose_name='site name', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_valid', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'web rich object',
                'verbose_name_plural': 'web rich objects',
            },
        ),
    ]
