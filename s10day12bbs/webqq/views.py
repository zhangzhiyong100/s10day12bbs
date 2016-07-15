#_*_coding:utf-8_*_

from django.shortcuts import render,HttpResponse
import json,datetime
# Create your views here.
import utils
import models

global_msg_dic = {}

def dashboard(request):
    return  render(request,'webqq/dashboard.html')


def send_msg(request):#发送消息

    print request.POST

    data = request.POST.get('data')#获取前端发送的数据
    #print json.loads(data)     #打印
    data = json.loads(data)
    data['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  #给date数据加上时间戳
    to_id = data.get('to_id')   #获取目标id
    user_obj = models.bbs_models.UserProfile.objects.get(id=to_id)  #根据to_id找到对应的用户
    contact_type = data.get('contact_type')   #获取目标类型
    if contact_type == 'single':
        if not global_msg_dic.has_key(to_id):
        #当有消息过来时，检测webserver的global_msg_dic是否有目标id即to_id，如果没有，执行utils模块，给用户创建一个queue
            global_msg_dic[to_id] = utils.Chat()#创建实例 ，初始化queue
        global_msg_dic[to_id].msg_queue.put(data)#put data
        print '\033[31;1mPush msg [%s] into user [%s] queue' %(data['msg'],user_obj.name)

    elif contact_type == 'group':
        group_obj = models.QQGroup.objects.get(id=to_id)
        for member in group_obj.members.select_related():
            if member.id != request.user.userprofile.id:
                if not global_msg_dic.has_key(member.id):
                #当有消息过来时，检测webserver的global_msg_dic是否有目标id即to_id，如果没有，执行utils模块，给用户创建一个queue
                    global_msg_dic[member.id] = utils.Chat()#创建实例 ，初始化queue
                global_msg_dic[member.id].msg_queue.put(data)#put data
                print '\033[31;1mPush msg [%s] into user [%s] queue' %(data['msg'],member.name)

    return HttpResponse("dddd")




def get_msg(request):
    uid = request.GET.get('uid')#先获取uid，即和谁对话
    if uid: #判断uid是否存在
        res = []
        if not global_msg_dic.has_key(uid):#判断global_msg_dic是否有uid的消息
            global_msg_dic[uid] = utils.Chat()
        res = global_msg_dic[uid].get_msg(request)
        return HttpResponse(json.dumps(res))
    else:
        return HttpResponse(json.dumps("uid not provided"))















