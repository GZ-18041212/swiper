import random

import  requests

from swiper import config
from worker import call_by_worker
from django.core.cache import cache

def gen_vertify_code(length=6):
    # random.randrange(100000,1000000)
    return random.randrange(10**(length-1),10**length)

@call_by_worker
def send_vertify_code(phonenum):
    vcode=gen_vertify_code()
    key='send_vertify_code-%s'%phonenum
    cache.set(key,vcode,120)
    sms_cfg=config.HY_MSM_PARAMS.copy()  #使用短信模板设置的浅拷贝
    sms_cfg['content']=sms_cfg['content']%vcode
    sms_cfg['mobile']=phonenum
    response=requests.post(config.HY_MSM_URL,data=sms_cfg).json()  #这个是访问URL并且提交内容的
    return response     #这个是request访问提交请求之后结果

# from django.utils.functional import
#requests还有django还flask这些都是第三方的，random是属于Pytho自带
#自带包=库最先写，第三方次之，自己写的最下面

def check_vcode():
    pass




























