#_*_coding:utf-8_*_

from django.shortcuts import render,HttpResponse
import json,datetime
# Create your views here.
import utils
import models

global_msg_dic = {}

def dashboard(request):
    return  render(request,'webqq/dashboard.html')


def send_msg(request):#������Ϣ

    print request.POST

    data = request.POST.get('data')#��ȡǰ�˷��͵�����
    #print json.loads(data)     #��ӡ
    data = json.loads(data)
    data['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  #��date���ݼ���ʱ���
    to_id = data.get('to_id')   #��ȡĿ��id
    user_obj = models.bbs_models.UserProfile.objects.get(id=to_id)  #����to_id�ҵ���Ӧ���û�
    contact_type = data.get('contact_type')   #��ȡĿ������
    if contact_type == 'single':
        if not global_msg_dic.has_key(to_id):
        #������Ϣ����ʱ�����webserver��global_msg_dic�Ƿ���Ŀ��id��to_id�����û�У�ִ��utilsģ�飬���û�����һ��queue
            global_msg_dic[to_id] = utils.Chat()#����ʵ�� ����ʼ��queue
        global_msg_dic[to_id].msg_queue.put(data)#put data
        print '\033[31;1mPush msg [%s] into user [%s] queue' %(data['msg'],user_obj.name)

    elif contact_type == 'group':
        group_obj = models.QQGroup.objects.get(id=to_id)
        for member in group_obj.members.select_related():
            if member.id != request.user.userprofile.id:
                if not global_msg_dic.has_key(member.id):
                #������Ϣ����ʱ�����webserver��global_msg_dic�Ƿ���Ŀ��id��to_id�����û�У�ִ��utilsģ�飬���û�����һ��queue
                    global_msg_dic[member.id] = utils.Chat()#����ʵ�� ����ʼ��queue
                global_msg_dic[member.id].msg_queue.put(data)#put data
                print '\033[31;1mPush msg [%s] into user [%s] queue' %(data['msg'],member.name)

    return HttpResponse("dddd")




def get_msg(request):
    uid = request.GET.get('uid')#�Ȼ�ȡuid������˭�Ի�
    if uid: #�ж�uid�Ƿ����
        res = []
        if not global_msg_dic.has_key(uid):#�ж�global_msg_dic�Ƿ���uid����Ϣ
            global_msg_dic[uid] = utils.Chat()
        res = global_msg_dic[uid].get_msg(request)
        return HttpResponse(json.dumps(res))
    else:
        return HttpResponse(json.dumps("uid not provided"))















