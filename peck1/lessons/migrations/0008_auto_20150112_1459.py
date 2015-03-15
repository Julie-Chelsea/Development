# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_auto_20150112_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='definition',
        ),
        migrations.AddField(
            model_name='word',
            name='def_2_exist',
            field=models.BooleanField(default=False, verbose_name='Another definition?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='word',
            name='def_3_exist',
            field=models.BooleanField(default=False, verbose_name='Another definition?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='word',
            name='definition_one',
            field=models.CharField(default='', max_length=200, verbose_name='Definition 1'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='word',
            name='definition_three',
            field=models.CharField(default='', max_length=200, verbose_name='Definition 3'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='word',
            name='definition_two',
            field=models.CharField(default='', max_length=200, verbose_name='Definition 2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='word',
            name='speech_level',
            field=models.CharField(default='Polite', max_length=200),
            preserve_default=True,
        ),
    ]
