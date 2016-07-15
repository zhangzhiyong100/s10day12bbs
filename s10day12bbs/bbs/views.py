#_*_coding:utf-8_*_
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import models
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
import utils
import json
from django.contrib.auth import authenticate,login

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.



def account_login(request):


    if request.method == 'GET':
        return  render(request,'login.html')

    else:
        print request.POST
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(username=username,password=passwd)
        if user is not None:
            login(request,user)
            user.userprofile.online = True
            user.userprofile.save()
            return  HttpResponseRedirect("/")
        else:
            return  render(request,'login.html',{
                'login_err': "Wrong username or password!"
            })


def index(request):
    article_list = models.Article.objects.all().order_by('-publish_date')#order_by是排序意思，-是倒序的意向，从新到旧
    paginator = Paginator(article_list,3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render(request,'index.html',{
        'articles': articles
    })

def article(request,article_id):#文章的视图，有时获取不到article_id，所以用try
    err_msg = ''
    try:
        article_obj = models.Article.objects.get(id=article_id)
        comments = utils.build_comments_tree(request)
    except ObjectDoesNotExist,e:
        err_msg = str(e)
    return render(request,'article.html',{
                    'article':article_obj,
                    'err_msg':err_msg,
                    'comments':comments
                 })

def create_article(request):
    if request.method == "GET":
        return render(request,'create_article.html')
    elif request.method =="POST":
        print request.FILES#在manage处获取网页提交的信息
        bbs_generater = utils.ArticleGen(request)#通过utils实现数据存入数据库
        res = bbs_generater.create()
        html_ele = '''Your article <<a href="/article/%s/">%s</a>>
         has been created successfully! ''' %(res.id,res.title)
        return HttpResponse(html_ele)

def life(request):

    return  render(request,'life.html')

def tech(request):

    return  render(request,'tech.html')

def category1024(request):

    return  render(request,'1024.html')