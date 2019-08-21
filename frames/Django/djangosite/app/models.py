from __future__ import unicode_literals
from django.db import models

# 新增元组用于设置消息类型枚举项
KIND_CHOICES = (
    ('Python技术', 'Python技术'),
    ('数据库技术', '数据库技术'),
    ('经济学', '经济学'),
    ('文体资讯', '文体资讯'),
    ('个人心情', '个人心情'),
    ('其他', '其他'),
)

class Moment(models.Model):
	content = models.CharField(max_length = 200)
	user_name =  models.CharField(max_length = 20)
	kind = models.CharField(max_length = 20, choices = KIND_CHOICES, default = KIND_CHOICES[0])

LEVELS = (
	('1', 'Very good'),
	('2', 'Good'),
	('3', 'Normal'),
	('4', 'Bad'),
)

class Comment(models.Model):
	id = models.AutoField(primary_key = True)
	headline = models.CharField(max_length = 255)
	body_text = models.TextField()
	pub_date = models.DateField()
	n_visits = models.IntegerField()
	level = models.CharField("请为本条信息评数", max_length = 1, choices = LEVELS)

	def __str__(self):
		return self.headline

'''
# 抽象类继承
class MessageBase(models.Model):
	id = models.AutoField()
	content = models.CharField(max_length = 100)
	user_name =  models.CharField(max_length = 80)
	pub_date = models.DateField()

	class Meta:
		abstract = True

class Moment(MessageBase):
	headline = models.CharField(max_length = 50)

class Comment(MessageBase):
	level = models.CharField(max_length = 1, choices = LEVELS)

'''

'''
# 多表继承
class MessageBase(models.Model):
	id = models.AutoField()
	content = models.CharField(max_length = 100)
	user_name =  models.CharField(max_length = 80)
	pub_date = models.DateField()

class Moment(MessageBase):
	headline = models.CharField(max_length = 50)

class Comment(MessageBase):
	level = models.CharField(max_length = 1, choices = LEVELS)
'''

'''
# 代理模型继承
class Comment(models.Model):
	id = models.AutoField()
	headline = models.CharField(max_length = 50)
	content = models.CharField(max_length = 100)
	user_name =  models.CharField(max_length = 80)
	pub_date = models.DateField()

class OrderedMoment(Moment):
	class Meta:
		proxy = True
		ordering = ["-pub_date"]
'''


class Account(models.Model):
	user_name = models.CharField(max_length = 80)
	password = models.CharField(max_length = 255)
	reg_date = models.DateField()

	def __unicode__(self):
		return "Account: %s" % self.user_name

class Contact(models.Model):
	'''
	#一对一
	account = models.OneToOneField(
		Account,
		on_delete = models.CASCADE,
		primary_key=True,
	)
	'''

	'''
	#一对多
	account = models.ForeignKey(Account, on_delete = models.CASCADE)
	'''

	# 多对多
	accounts = models.ManyToManyField(Account)
	zip_code = models.CharField(max_length = 10)
	address = models.CharField(max_length = 80)
	mobile = models.CharField(max_length = 20)

	def __unicode__(self):
		return "%s, %s" % (self.account.user_name, mobile)

