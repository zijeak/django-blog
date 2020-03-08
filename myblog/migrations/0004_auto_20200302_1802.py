# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_post_head_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='head_img',
            field=models.ImageField(upload_to='head_img'),
        ),
    ]
