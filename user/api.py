import json
import sys   #改过的
from lib.http import  render_json
from django.shortcuts import render
from django.http import HttpResponse

from logic import  send_vertify_code,gen_vertify_code
from django.core.cache import cache

# Create your views here.

# get_vertify_code():

def get_vertify_code(request):    #其实返回render返回的也是HTTPRESPONSE
    #手机注册
    phonenum=request.POST.get('phonenum')
    send_vertify_code(phonenum)
    return render_json(None,0)


def login(request):
    #短信验证码登录
    cache.get(key)
    pass

def get_profile(request):
    #获取个人资料
    pass
def modify_profile(request):
    #修改个人资料
    pass
def get_avatar(reqeust):
    #头像上传
    pass

