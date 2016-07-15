#from __future__ import unicode_literals
#_*_coding:utf-8_*_
from django.db import models
from bbs import models as bbs_models
# Create your models here.

class QQGroup(models.Model):
    name = models.CharField(max_length=64) #Ⱥ��
    founder = models.ForeignKey(bbs_models.UserProfile,)#��ʼ��
    brief = models.TextField(max_length=1024,default="nothing...")#Ⱥ����
    admin = models.ManyToManyField(bbs_models.UserProfile,related_name='group_admin') #����Ա
    members= models.ManyToManyField(bbs_models.UserProfile,related_name='group_numbers')#��������
    members_limit = models.IntegerField(default=200)#Ⱥ��������200
    def __unicode__(self):
        return self.name


