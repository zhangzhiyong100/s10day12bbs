#_*_coding:utf-8_*_
__author__ = 'zhangzhiyong'

import Queue

class Chat(object):
    def __init__(self):
        self.msg_queue = Queue.Queue()

    def get_msg(self,request):
        new_msgs = []
        if self.msg_queue.qsize()>0:    #消息队列大于0，表示有消息
            for msg in range(self.msg_queue.qsize()):#for循环 一次取一条
                new_msgs.append(self.msg_queue.get_nowait())
        else:#no new msg ,but wait for 60 secs
            try:
                print '-----no new msg,going to wait for 60 secs-----'
                new_msgs.append(self.msg_queue.get(timeout=6))
                print "\033[32;1m Found  new msgs\033[0m",new_msgs
            except Queue.Empty:
                print "\033[031;1m Time out, no new msg for user[%s]\033[0m"%request.user.userprofile.name
        print "\033[33;1m Found [%s] new msgs\033[0m"%len(new_msgs)
        return new_msgs





