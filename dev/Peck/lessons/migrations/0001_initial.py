# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drama',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fill_In_Blank_Answer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('answer', models.CharField(verbose_name='Potential answer', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fill_In_Blank_Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('instruction', models.CharField(verbose_name='Instructions', max_length=200, default='Fill in the blanks with the correct answer.')),
                ('question', models.CharField(verbose_name='Question', max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('number', models.PositiveIntegerField(verbose_name='Lesson #', default=0)),
                ('title', models.CharField(verbose_name='Lesson', max_length=30)),
                ('url', models.URLField(blank=True, default='')),
                ('language', models.CharField(verbose_name='Language', max_length=30, default='Korean', choices=[('KOR', 'Korean'), ('JPN', 'Japanese')])),
                ('published', models.DateTimeField(verbose_name='Date published', default=django.utils.timezone.now)),
                ('visible', models.BooleanField(verbose_name='Show?', default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Long_Translate_Answer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('answer', models.CharField(verbose_name='Potential answer', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Long_Translate_Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('instruction', models.CharField(verbose_name='Instructions', max_length=200, default='Translate the word/phrase into English.')),
                ('question', models.CharField(verbose_name='Question', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Matching_Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('instruction', models.CharField(verbose_name='Instructions', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Multiple_Choice_Answer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('answer', models.CharField(verbose_name='Option', max_length=200)),
                ('correct', models.BooleanField(verbose_name='Correct?', default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Multiple_Choice_Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('question', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pair1',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('item', models.CharField(verbose_name='Pair 1', max_length=100)),
                ('question', models.ForeignKey(to='lessons.Matching_Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pair2',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('item', models.CharField(verbose_name='Pair 2', max_length=100)),
                ('question', models.ForeignKey(to='lessons.Pair1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('lesson', models.OneToOneField(serialize=False, primary_key=True, to='lessons.Lesson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Short_Translate_Answer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('answer', models.CharField(verbose_name='Potential answer', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Short_Translate_Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('question', models.CharField(max_length=200)),
                ('true', models.BooleanField(verbose_name='True?', default=False)),
                ('quiz', models.ForeignKey(to='lessons.Quiz')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('URL', models.URLField(default='http://')),
                ('instruction', models.CharField(verbose_name='Instructions', max_length=200, default='Play the clips and answer the question(s).')),
                ('quiz', models.ForeignKey(to='lessons.Quiz')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video_Answer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('answer', models.CharField(verbose_name='Potential answer', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video_Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('start_time', models.CharField(max_length=10, default='00:00:00')),
                ('stop_time', models.CharField(max_length=10, default='00:00:00')),
                ('question', models.CharField(max_length=200)),
                ('video', models.ForeignKey(to='lessons.Video')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('word', models.CharField(verbose_name='Word/Phrase', max_length=200)),
                ('romanization', models.CharField(blank=True, max_length=200, default='')),
                ('definition_one', models.CharField(verbose_name='Definition 1', max_length=200, default='')),
                ('def_2_exist', models.BooleanField(verbose_name='Another definition?', default=False)),
                ('definition_two', models.CharField(blank=True, verbose_name='Definition 2', max_length=200, default='')),
                ('def_3_exist', models.BooleanField(verbose_name='Another definition?', default=False)),
                ('definition_three', models.CharField(blank=True, verbose_name='Definition 3', max_length=200, default='')),
                ('speech_level', models.CharField(max_length=200, default='Dictionary')),
                ('img', models.URLField(blank=True)),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='video_answer',
            name='question',
            field=models.ForeignKey(to='lessons.Video_Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='short_translate_answer',
            name='question',
            field=models.ForeignKey(to='lessons.Short_Translate_Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='multiple_choice_question',
            name='quiz',
            field=models.ForeignKey(to='lessons.Quiz'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='multiple_choice_answer',
            name='question',
            field=models.ForeignKey(to='lessons.Multiple_Choice_Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matching_question',
            name='quiz',
            field=models.ForeignKey(to='lessons.Quiz'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='long_translate_question',
            name='quiz',
            field=models.ForeignKey(to='lessons.Quiz'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='long_translate_answer',
            name='question',
            field=models.ForeignKey(to='lessons.Long_Translate_Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fill_in_blank_question',
            name='quiz',
            field=models.ForeignKey(to='lessons.Quiz'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fill_in_blank_answer',
            name='question',
            field=models.ForeignKey(to='lessons.Fill_In_Blank_Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entertainment',
            name='lesson',
            field=models.ForeignKey(to='lessons.Lesson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drama',
            name='entertainment',
            field=models.ForeignKey(to='lessons.Entertainment'),
            preserve_default=True,
        ),
    ]
