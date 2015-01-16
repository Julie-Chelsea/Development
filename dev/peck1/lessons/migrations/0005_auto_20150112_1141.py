# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_auto_20150112_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson_number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson_name',
            new_name='title',
        ),
    ]
