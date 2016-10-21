# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
# Create your models here.


@python_2_unicode_compatible
class Article(models.Model):
	# id = models.IntegerField('博文编号', primary_key=True, auto_created=True)
	id = models.AutoField(primary_key=True)
	title = models.CharField('标题', max_length=256)
	content = models.TextField('内容', max_length=500, db_index=True)
	type = models.CharField('类型', max_length=256,)
	published_time = models.DateTimeField('发布时间')
	update_time = models.DateTimeField('更新时间')

	def get_absolute_url(self):
		path = reverse('blog_detail', kwargs={'blog_id': self.id})
		return "http://127.0.0.1:8000%s" % path

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-published_time']

