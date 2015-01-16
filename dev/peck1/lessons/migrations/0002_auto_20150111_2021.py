# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='url',
            field=models.URLField(default='lesson/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='URL',
            field=models.URLField(default='http://'),
        ),
        migrations.AlterField(
            model_name='word',
            name='img',
            field=models.URLField(default='img/lesson/no1/.svg'),
        ),
    ]
