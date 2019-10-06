from django.shortcuts import render, HttpResponse

# Create your views here.
# .表示当前包下的models
from .models import MongoModel
from django.views.generic import View
from blog.views import CommonViewMixin
from django.views.generic import ListView
import json
from django.http import JsonResponse
import datetime
import time

start_time = ''
end_time = ''

class MongoView(CommonViewMixin, ListView):
    # def get(self, request):
    #     #MongoModel.objects.create(name='水痕', age= 20)
    #     result = MongoModel.objects.filter(value__gte=11112, value__lte=100000)

    #     ### for debug
    #     # result = MongoModel.objects.all()
    #     # for i in range( result.count() ):
    #     #     print(result[i].value)
    #     # print(result[0].value)
    #     # str_res = []
    #     # for i in range( result.count() ):
    #     #     str_res += str( result[i].value ) + '\r\n'

    #     return HttpResponse(result)
    
    queryset = MongoModel.objects.all()
    template_name = 'mongo/mongo.html'
    context_object_name = 'data'

    default_start_time = '2019.01.31 - 04:00 pm'
    default_end_time = '2019.03.31 - 04:22 pm'
    

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)
        
        global start_time, end_time
        start_time_d = self.default_start_time
        end_time_d = self.default_end_time

        start_time = self.request.GET.get('start_time')
        end_time = self.request.GET.get('end_time')

        if start_time:
            context.update({
                'start_time': start_time
            })
        else:
            context.update({
                'start_time': start_time_d
            })

        if end_time:
            context.update({
                'end_time': end_time
            })
        else:
            context.update({
                'end_time': end_time_d
            })

        return context


def mongo_data(request):

    global start_time, end_time

    st = ''
    if start_time:
        start_t = start_time[:-3]
        st = datetime.datetime.strptime(start_t, "%Y.%m.%d - %H:%M")

        if(start_time[-2:]=='pm'):
            st = st + datetime.timedelta(hours=12)
    
    et = ''
    if end_time:
        end_t = end_time[:-3]
        et = datetime.datetime.strptime(end_t, "%Y.%m.%d - %H:%M")

        if(end_time[-2:]=='pm'):
            et = et + datetime.timedelta(hours=12)

    if st and et:
        # result = MongoModel.objects.filter(value__gte=11112, value__lte=100000)
        result = MongoModel.objects.filter(Date__gte=st, Date__lte=et).order_by('Date')
        cnt = result.count()

        print( type(result[0].Date) )
        print( result[0].Date )

        x = []
        for i in range( result.count() ):
            x.append( str( result[i].Date) )

        y1 = []
        for i in range( result.count() ):
            y1.append(result[i].id)

        y = []
        for i in range( result.count() ):
            y.append(result[i].value)

        jsondata = {
            "key": x,
            "id": y1,
            "value": y,
        }
    else:
        jsondata = {}

    return JsonResponse(jsondata)
