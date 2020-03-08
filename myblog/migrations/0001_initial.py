# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='分类名', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='文章标题', max_length=200)),
                ('content', models.TextField(verbose_name='文章正文', null=True)),
                ('created_time', models.DateTimeField(verbose_name='发表时间')),
                ('modified_time', models.DateTimeField(verbose_name='最后修改时间')),
                ('excerpt', models.CharField(verbose_name='文章摘要', max_length=200, blank=True)),
                ('author', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name='分类', to='myblog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='标签名', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ForeignKey(verbose_name='标签', blank=True, to='myblog.Tag'),
        ),
    ]
