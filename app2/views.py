import os.path
import time

from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.db.models import Max, F, Q
from django.contrib.auth import logout
from django.core.paginator import Paginator


# Create your views here.
from app2.models import Grades, Students
def index(request) :  # 表示的是请求体
    return render(request,'app2/index.html')


def detail(request, num, num2) :  # 表示接受数字
    return HttpResponse("detail-%s-%s" % (num, num2))

def upfile(request):
    return render(request,'app2/upfile.html')

def savefile(request):
    if request.method=="POST":
        f=request.FILES['file']  #拿出文件,是一个文件流
        filePath=os.path.join(settings.MEDIA_ROOT,f.name)  #表示合成文件在服务器端的路径,即想存在哪个目录下面
        with open(filePath,'wb') as fp:
            for info in f.chunks():  #此处表示的是给文件分段,接受文件的一部分
                fp.write(info)
        return HttpResponse("上传成功")
    else:
        return HttpResponse("上传失败")


def studentPage(request,pageid):
    #显示的是所有学生的列表
    allList=Students.stuObj1.all()
    #分页显示
    paginator=Paginator(allList,2)
    #取出页码
    page=paginator.page(pageid)
    #显示个数
    #lenth=len(page)
    return render(request,'app2/studentPage.html',{'students':page})

def ajaxstudent(request):
    return render(request,'app2/ajaxstudent.html')

from django.http import JsonResponse
def studentinfo(request):

    stus=Students.stuObj1.all()
    list=[]
    for stu in stus:
        list.append([stu.sname,stu.sage])
    return JsonResponse({"data":list})
# 在页面里面使用富文本
def edit(request):
    return render(request,'app2/edit.html')
import time
def celery(request):
    #耗时操作,所以将下面的写到task里面
    print("go")
    time.sleep(5)

    return render(request,'app2/celery.html')