# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20200302_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=mdeditor.fields.MDTextField(default='default content'),
        ),
    ]
