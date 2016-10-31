# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('video_id', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('video_title', models.CharField(max_length=400)),
                ('video_description', models.TextField(max_length=2000)),
            ],
            options={
                'db_table': 'youtube_videos',
                'managed': True,
            },
        ),
    ]
