#_*_coding:utf-8_*_
__author__ = 'zhang'
import models
from s10day12bbs import settings

class ArticleGen(object):#�����Ķ���ҳ�ύ������������
    def __init__(self,request):#��ȡ��ҳ�ύ������
        self.request = request



    def parse_data(self):#����ҳ�ύ������ȡ���ؼ�����
        form_data = {
        'title' : self.request.POST.get('title'),
        'content' : self.request.POST.get('content'),
        'category_id': 1,
        'summary' : self.request.POST.get('summary'),
        'author_id': self.request.user.userprofile.id,
        'head_img':' ',
        }
        return form_data
    def create(self):#������ȡ�Ĺؼ����ݣ��������ݵ����ݿ���
        self.data = self.parse_data()
        bbs_obj=models.Article(**self.data)#�����ݴ���models.Article��ģ����
        bbs_obj.save()#�����ݿⱣ��
        filename = handle_upload_file(self.request,self.request.FILES['head_img'])
        bbs_obj.head_img = 'imgs/upload/%s' % filename
        bbs_obj.save()

        return bbs_obj


    def update(self):
        pass



def handle_upload_file(request,file_obj):#�����ϴ����ļ�
    upload_dir = '%s/%s'%(settings.BASE_DIR,settings.FileUploadDir)

    print '-->',dir(file_obj)
    with open('%s/%s'%(upload_dir,file_obj.name),'wb') as destination:
        for chunk in file_obj.chunks():#chunks����readline
            destination.write(chunk)

    return file_obj.name

def recursive_search(data_dic,comment):
    for parent,v in data_dic.items():
        if parent == comment.parent_comment:
            print "find parent of [%s]" % comment
            data_dic[comment.parent_comment][comment] = {}
        else:
            print "cannot find [%s]'s parent,going to furhter layer" % comment, data_dic[parent]
            recursive_search(data_dic[parent],comment)



def build_comments_tree(request):
    bbs_obj = models.Article.objects.first()
    print bbs_obj.comment_set.select_related()
    tree_dic = {}
    for comment in bbs_obj.comment_set.select_related().order_by('id'):
        if not comment.parent_comment: #no farther ,first layer
            tree_dic[comment] ={}
        else:
            recursive_search(tree_dic,comment)
    return tree_dic

    for k,v in tree_dic.items():
        print '------>',k,v





'''
{
    A :{
        A2:{
            A3:{
                A4:{}
            },
            A3-2:{},
            A3-3:{
                A3-3-2:{}
            },

        },
        A2-2:{},
    }
}

A none
A2 A
A3 A2
A4 A3
A2-2 A
A3-2 A2
A3-3 A2
A3-3-2 A3-3

B None
B2 B

'''



































































