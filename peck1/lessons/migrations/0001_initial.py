# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('definition', models.CharField(verbose_name='Definition', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fill_In_Answers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('answer', models.CharField(verbose_name='Potential answer', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fill_In_Blank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('instruction', models.CharField(default='Fill in the blanks with the correct answer.', verbose_name='Instructions', max_length=200)),
                ('question', models.CharField(verbose_name='Question', max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lesson_number', models.PositiveIntegerField(default=0, verbose_name='Lesson #')),
                ('lesson_name', models.CharField(verbose_name='Lesson', max_length=30)),
                ('language', models.CharField(default='Korean', verbose_name='Language', choices=[('KOR', 'Korean'), ('JPN', 'Japanese')], max_length=30)),
                ('published', models.DateTimeField(verbose_name='Date published')),
                ('visible', models.BooleanField(default=False, verbose_name='Show?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Long_Translate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('instruction', models.CharField(default='Translate the word/phrase into English.', verbose_name='Instructions', max_length=200)),
                ('question', models.CharField(verbose_name='Question', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Long_Translate_Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('answer', models.CharField(verbose_name='Potential answer', max_length=200)),
                ('question', models.ForeignKey(to='lessons.Long_Translate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Matching_Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('instruction', models.CharField(verbose_name='Instructions', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Multiple_Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Multiple_Choice_Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('answer', models.CharField(verbose_name='Option', max_length=200)),
                ('correct', models.BooleanField(default=False, verbose_name='Correct?')),
                ('question', models.ForeignKey(to='lessons.Multiple_Choice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pair1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('lesson', models.OneToOneField(serialize=False, to='lessons.Lesson', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Short_Translate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('instruction', models.CharField(default='Translate the word/phrase into English.', verbose_name='Instructions', max_length=200)),
                ('question', models.CharField(verbose_name='Question', max_length=200)),
                ('quiz', models.ForeignKey(to='lessons.Quiz')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Short_Translate_Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('answer', models.CharField(verbose_name='Potential answer', max_length=200)),
                ('question', models.ForeignKey(to='lessons.Short_Translate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='True_False',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question', models.CharField(max_length=200)),
                ('true', models.BooleanField(default=False, verbose_name='True?')),
                ('quiz', models.ForeignKey(to='lessons.Quiz')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('URL', models.URLField()),
                ('instruction', models.CharField(default='Play the clips and answer the question(s).', verbose_name='Instructions', max_length=200)),
                ('quiz', models.ForeignKey(to='lessons.Quiz')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video_Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question', models.CharField(max_length=200)),
                ('video', models.ForeignKey(to='lessons.Video')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video_Question_Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('answer', models.CharField(verbose_name='Potential answer', max_length=200)),
                ('question', models.ForeignKey(to='lessons.Video_Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('word', models.CharField(max_length=200)),
                ('img', models.URLField()),
                ('definitions', models.ManyToManyField(to='lessons.Definition')),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='multiple_choice',
            name='quiz',
            field=models.ForeignKey(to='lessons.Quiz'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matching_question',
            name='quiz',
            field=models.ForeignKey(to='lessons.Quiz'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='long_translate',
            name='quiz',
            field=models.ForeignKey(to='lessons.Quiz'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fill_in_blank',
            name='quiz',
            field=models.ForeignKey(to='lessons.Quiz'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fill_in_answers',
            name='question',
            field=models.ForeignKey(to='lessons.Fill_In_Blank'),
            preserve_default=True,
        ),
    ]
