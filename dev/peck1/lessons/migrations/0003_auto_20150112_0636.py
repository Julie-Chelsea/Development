# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20150111_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drama',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fill_In_Blank_Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('answer', models.CharField(verbose_name='Potential answer', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fill_In_Blank_Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('instruction', models.CharField(verbose_name='Instructions', max_length=200, default='Fill in the blanks with the correct answer.')),
                ('question', models.CharField(verbose_name='Question', max_length=500)),
                ('quiz', models.ForeignKey(to='lessons.Quiz')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Long_Translate_Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('instruction', models.CharField(verbose_name='Instructions', max_length=200, default='Translate the word/phrase into English.')),
                ('question', models.CharField(verbose_name='Question', max_length=200)),
                ('quiz', models.ForeignKey(to='lessons.Quiz')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Multiple_Choice_Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('quiz', models.ForeignKey(to='lessons.Quiz')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Short_Translate_Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('instruction', models.CharField(verbose_name='Instructions', max_length=200, default='Translate the word/phrase into English.')),
                ('question', models.CharField(verbose_name='Question', max_length=200)),
                ('quiz', models.ForeignKey(to='lessons.Quiz')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('artist', models.CharField(verbose_name='Artist', max_length=50)),
                ('name', models.CharField(verbose_name='Song name', max_length=100)),
                ('URL', models.URLField(default='http://')),
                ('entertainment', models.ForeignKey(to='lessons.Entertainment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Song_Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('genre', models.CharField(verbose_name='Song genre', max_length=50)),
                ('song', models.ForeignKey(to='lessons.Song')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='True_False_Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('true', models.BooleanField(verbose_name='True?', default=False)),
                ('quiz', models.ForeignKey(to='lessons.Quiz')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video_Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('answer', models.CharField(verbose_name='Potential answer', max_length=200)),
                ('question', models.ForeignKey(to='lessons.Video_Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='fill_in_answers',
            name='question',
        ),
        migrations.DeleteModel(
            name='Fill_In_Answers',
        ),
        migrations.RemoveField(
            model_name='fill_in_blank',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Fill_In_Blank',
        ),
        migrations.RemoveField(
            model_name='long_translate',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='multiple_choice',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='short_translate',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='true_false',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='True_False',
        ),
        migrations.RemoveField(
            model_name='video_question_answer',
            name='question',
        ),
        migrations.DeleteModel(
            name='Video_Question_Answer',
        ),
        migrations.AddField(
            model_name='fill_in_blank_answer',
            name='question',
            field=models.ForeignKey(to='lessons.Fill_In_Blank_Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drama',
            name='entertainment',
            field=models.ForeignKey(to='lessons.Entertainment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video_question',
            name='start_time',
            field=models.CharField(max_length=10, default='00:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video_question',
            name='stop_time',
            field=models.CharField(max_length=10, default='00:00:00'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='long_translate_answer',
            name='question',
            field=models.ForeignKey(to='lessons.Long_Translate_Question'),
        ),
        migrations.DeleteModel(
            name='Long_Translate',
        ),
        migrations.AlterField(
            model_name='multiple_choice_answer',
            name='question',
            field=models.ForeignKey(to='lessons.Multiple_Choice_Question'),
        ),
        migrations.DeleteModel(
            name='Multiple_Choice',
        ),
        migrations.AlterField(
            model_name='short_translate_answer',
            name='question',
            field=models.ForeignKey(to='lessons.Short_Translate_Question'),
        ),
        migrations.DeleteModel(
            name='Short_Translate',
        ),
    ]
