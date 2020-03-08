# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20200302_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='head_img',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
