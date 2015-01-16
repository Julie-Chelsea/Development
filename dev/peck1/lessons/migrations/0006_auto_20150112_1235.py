# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_auto_20150112_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='definitions',
        ),
        migrations.DeleteModel(
            name='Definition',
        ),
        migrations.AddField(
            model_name='word',
            name='definition',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='word',
            name='img',
            field=models.URLField(),
        ),
    ]
