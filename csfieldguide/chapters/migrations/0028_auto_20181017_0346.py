# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-17 03:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0027_auto_20181011_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='introduction_xx_lr',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='introduction_yy_rl',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='name_xx_lr',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='name_yy_rl',
        ),
        migrations.RemoveField(
            model_name='chaptersection',
            name='content_xx_lr',
        ),
        migrations.RemoveField(
            model_name='chaptersection',
            name='content_yy_rl',
        ),
        migrations.RemoveField(
            model_name='chaptersection',
            name='name_xx_lr',
        ),
        migrations.RemoveField(
            model_name='chaptersection',
            name='name_yy_rl',
        ),
        migrations.RemoveField(
            model_name='glossaryterm',
            name='definition_xx_lr',
        ),
        migrations.RemoveField(
            model_name='glossaryterm',
            name='definition_yy_rl',
        ),
        migrations.RemoveField(
            model_name='glossaryterm',
            name='term_xx_lr',
        ),
        migrations.RemoveField(
            model_name='glossaryterm',
            name='term_yy_rl',
        ),
    ]
