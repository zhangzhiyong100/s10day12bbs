#_*_coding:utf-8_*_
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=254)
    category = models.ForeignKey('Category')#����,
    content = models.TextField(max_length=100000)
    author = models.ForeignKey('UserProfile')
    summary = models.TextField(max_length=500)#���
    head_img = models.ImageField(upload_to="statics/imgs/upload")
    publish_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Category(models.Model):#�����
    name = models.CharField(unique=True,max_length=64)
    admins = models.ManyToManyField('UserProfile')#��������ѡ
    def __unicode__(self):
        return self.name

class ThumbUP(models.Model):#����
    article = models.ForeignKey('Article')#һ�Զ�,����˶�һƪ���µ���
    user = models.ForeignKey('UserProfile')#�������ĸ��û�����
    data = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.article.title

class Comment(models.Model):#���۱�
    article = models.ForeignKey('Article')#һ�Զ�,����˶�һƪ���µ���
    user = models.ForeignKey('UserProfile')
    parent_comment = models.ForeignKey('self',blank=True,null=True,related_name='pid')#�����۹����Լ�������Ϊ��,blank��adminҳ����Կգ�null�����ݿ�����Կ�
#'self'��ʾ�����Լ����������related_name
    comment = models.TextField(max_length=1024)#����Ϊ��
    data = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.comment


class UserProfile(models.Model):#y�û���
    user = models.OneToOneField(User)  #һ��һ����django���û���֤
    name = models.CharField(max_length=32)
    user_groups = models.ManyToManyField('UserGroup')
    friends = models.ManyToManyField('self',blank=True,related_name='my_friend',symmetrical=True)#�����Լ�������Ϊ�գ����뽻related_name���Գƹ�ϵ
#friends���������ҵ��ֶΣ����û���Ϣ����ȥ
    def __unicode__(self):
        return self.name

class UserGroup(models.Model):#�û���
    name = models.CharField(max_length=32,unique=True)

    def __unicode__(self):
        return self.name