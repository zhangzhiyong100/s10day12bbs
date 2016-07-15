#_*_coding:utf-8_*_
from django.contrib import admin
import models
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','parent_comment','article')
admin.site.register(models.Article)#注册表，使可以在admin页面管理
admin.site.register(models.Category)
admin.site.register(models.ThumbUP)
admin.site.register(models.Comment)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)