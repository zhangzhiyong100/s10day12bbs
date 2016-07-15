#_*_coding:utf-8_*_
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=254)
    category = models.ForeignKey('Category')#分类,
    content = models.TextField(max_length=100000)
    author = models.ForeignKey('UserProfile')
    summary = models.TextField(max_length=500)#简介
    head_img = models.ImageField(upload_to="statics/imgs/upload")
    publish_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Category(models.Model):#分类表
    name = models.CharField(unique=True,max_length=64)
    admins = models.ManyToManyField('UserProfile')#版主，必选
    def __unicode__(self):
        return self.name

class ThumbUP(models.Model):#点赞
    article = models.ForeignKey('Article')#一对多,多个人对一篇文章点赞
    user = models.ForeignKey('UserProfile')#关联是哪个用户点赞
    data = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.article.title

class Comment(models.Model):#评论表
    article = models.ForeignKey('Article')#一对多,多个人对一篇文章点赞
    user = models.ForeignKey('UserProfile')
    parent_comment = models.ForeignKey('self',blank=True,null=True,related_name='pid')#父评论关联自己，可以为空,blank是admin页面可以空，null是数据库里可以空
#'self'表示关联自己，必须添加related_name
    comment = models.TextField(max_length=1024)#不能为空
    data = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.comment


class UserProfile(models.Model):#y用户表
    user = models.OneToOneField(User)  #一对一，用django的用户认证
    name = models.CharField(max_length=32)
    user_groups = models.ManyToManyField('UserGroup')
    friends = models.ManyToManyField('self',blank=True,related_name='my_friend',symmetrical=True)#关联自己，可以为空，必须交related_name，对称关系
#friends用于聊天室的字段，把用户信息传过去
    def __unicode__(self):
        return self.name

class UserGroup(models.Model):#用户组
    name = models.CharField(max_length=32,unique=True)

    def __unicode__(self):
        return self.name