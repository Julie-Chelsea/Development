# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_auto_20150112_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='romanization',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
