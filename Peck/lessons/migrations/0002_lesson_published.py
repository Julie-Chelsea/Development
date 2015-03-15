# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='published',
            field=models.DateTimeField(verbose_name='Date published', default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
