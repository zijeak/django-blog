from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.core.urlresolvers import reverse
import django.utils.timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='分类名')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50,verbose_name='标签名')
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='文章标题')
    # content = models.TextField(verbose_name='文章正文',null=True)
    content = MDTextField(default='default content')
    created_time = models.DateTimeField(verbose_name='发表时间')
    modified_time = models.DateTimeField(verbose_name='最后修改时间')
    date = models.DateField(verbose_name='发表日期',default=django.utils.timezone.now)
    excerpt = models.CharField(max_length=200, blank=True,verbose_name='文章摘要')
    head_img = models.ImageField(upload_to='head_img')

    category = models.ForeignKey(Category,verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User,verbose_name='作者')