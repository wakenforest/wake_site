from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from blog.views import CommonViewMixin
from .models import Link

from django.http import JsonResponse
import random

import threading
import time
from django.views.decorators.csrf import csrf_exempt
import json
 

class LinkListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'


def index(request):
    return render(request, 'index.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def ajax_list(request):
    a = list( range(100) )
    return HttpResponse(json.dumps(a), content_type='application/json')

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')

class IntroView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/intro.html'
    context_object_name = 'self_intro'

# class DataView(CommonViewMixin, ListView):
#     queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
#     template_name = 'config/data.html'
#     context_object_name = 'data'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         data1 = range(0,10)
#         print(data1)
#         context.update({
#             'data1': data1,
#         })
#         return context

class DataView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/data.html'
    context_object_name = 'data'

    x = list( range(0,30) ) 
    ylist =  [0 for _ in range(30)]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data1 = range(0,10)
        print(data1)
        context.update({
            'data1': data1,
        })
        return context

    # def thread_func(self):
    #     n = 25 + random.randint(0, 10)
    #     for i in range(29):
    #         self.ylist[i] = self.ylist[i+1]
    #     self.ylist[29] = n
    
    # def echarts_data(self,request):

    #     timer = threading.Timer(1, self.thread_func)
    #     timer.start()
        
    #     jsondata = {
    #         "key": self.x,
    #         "value": self.ylist,
    #     }
    #     return JsonResponse(jsondata) 


dataLen = 50
ylist =  [0 for _ in range(dataLen)]

def thread_func():
    global ylist,dataLen
    n = -4 + random.randint(0, 10)
    ylist[dataLen-1] = ylist[dataLen-1] + n
    for i in range(dataLen-1):
        ylist[i] = ylist[i+1]

    # for i in range(dataLen-1):
    #     ylist[i] = ylist[i+1]
    # ylist[dataLen-1] = n

    #print(ylist)
    
def echarts_data(request):
    global dataLen
    x = list( range(0,dataLen) ) 
    # y = list( range(0,10) ) 

    # for i in range(10):
    #     n = random.randint(0, 2 ^ 31 - 1)
    #     ylist.append(n)
    
    timer = threading.Timer(1, thread_func)
    timer.start()
    
    jsondata = {
        "key": x,
        "value": ylist,
    }
    return JsonResponse(jsondata)