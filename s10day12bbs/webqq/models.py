#from __future__ import unicode_literals
#_*_coding:utf-8_*_
from django.db import models
from bbs import models as bbs_models
# Create your models here.

class QQGroup(models.Model):
    name = models.CharField(max_length=64) #群名
    founder = models.ForeignKey(bbs_models.UserProfile,)#创始人
    brief = models.TextField(max_length=1024,default="nothing...")#群介绍
    admin = models.ManyToManyField(bbs_models.UserProfile,related_name='group_admin') #管理员
    members= models.ManyToManyField(bbs_models.UserProfile,related_name='group_numbers')#管理人数
    members_limit = models.IntegerField(default=200)#群人数限制200
    def __unicode__(self):
        return self.name


