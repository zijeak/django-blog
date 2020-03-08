# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20200303_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(verbose_name='发表日期', default=datetime.datetime(2020, 3, 4, 22, 5, 55, 590726)),
        ),
    ]
