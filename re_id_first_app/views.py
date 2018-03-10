from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import os
from django.views.decorators.http import require_http_methods
from datetime import datetime
from django.template import Template, Context
from . import rank


def img_proc(request):
    datalist = []
    if request.method == 'GET':
        img_dir = request.GET.get("img_dir", None)
        print(img_dir)
        time = datetime.now()
        if img_dir is not None:
            rank.rank_save(img_dir)
            with open('matching_info.txt', "r") as f:
                with open('img_info.txt', 'a+') as f2:
                    f2.write("{}--{}\n".format(img_dir, time.strftime("%y-%m-%d %H:%M:%S")))
                cnt = 0
                rawContent = f.read()
                rawContent = rawContent.split(' ')
                for line in rawContent:
                    cnt = cnt + 1
                    final_dir = ("image/Market-1501-v15.09.15/bounding_box_test/" + line)
                    d = {"index": cnt,
                         "dir": final_dir
                         }
                    datalist.append(d)
                    if cnt >= 10:
                        break

    return render(request, 're_id_first_app/re_id.html', {'data': datalist})


def home(request):
    info_dict = {'site': 'This is my site', 'content': 'A lot of things here'}
    return render(request, 're_id_first_app/test.html', {'info_dict': info_dict})


def img_proc_test(request):
    datalist = []
    if request.method == 'GET':
        img_dir = request.GET.get("img_dir", None)
        # print(img_dir)
        time = datetime.now()
        if img_dir is not None:
            rank.rank_save(img_dir)
            with open('matching_info.txt', "r") as f:
                with open('img_info.txt', 'a+') as f2:
                    f2.write("{}--{}\n".format(img_dir, time.strftime("%y-%m-%d %H:%M:%S")))
                cnt = 0
                rawContent = f.read()
                rawContent = rawContent.split(' ')
                for line in rawContent:
                    cnt = cnt + 1
                    final_dir = ("image/Market-1501-v15.09.15/bounding_box_test/" + line)
                    d = {"index": cnt,
                         "dir": final_dir
                         }
                    print(final_dir)
                    datalist.append(d)
                    if cnt >= 10:
                        break
                        print('------------------------')
                        print('ssss'+ datalist[0])
    return render(request, 're_id_first_app/re_id.html', {'data': datalist})
