"""swiper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 接口文件
# import sys   #修改过的
import sys
import os

# from django.shortcuts import render

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from django.contrib import admin   #原本有，修改过
from django.urls import path     #原本有，修改过
# from django.conf.urls import url  #新增
# from  user.logic  import  send_vertify_code  #通过这种方式才能导入
# from user_api   import  get_vertify_code
# from logic1 import send_vertify_code

# from user import  api as user_api    #0705修改导入过
from user.logic  import  send_vertify_code,gen_vertify_code   #不可以通过第三方文件导入，直接导入诶成
# import user yanzhengmatest3
# from user import yanzhengmatest3  D:\Classes\GZ-1804\src\swiper\user\yanzhengmatest3.html


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('admin/', admin.site.urls),
    # path(r'^/user/vertify_code', user_api.get_vertify_code),   #0705修改过
    # url(r'^/user/vertify_code', user_api.get_vertify_code),  # 0705修改过
    # path('/user/vertify_code', user_api.get_vertify_code),   #0705修改过
    # path('admin/', admin.site.urls),
# path('/localhost:8000/api/user/verfify', admin.site.urls),
#     path('/api/user/verfify', send_vertify_code),
    path('api/user/verfify', gen_vertify_code),

 ]
# def re():
#     return render('yanzhengmatest3.html',None)
# re()

# urlpatterns = [ path('admin/', admin.site.urls), path('app/', include('gen_vertify_code')), ]








