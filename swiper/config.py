'''
第三方平台的一些配置，第三方的一些配置是用config额，自己本身django的配置是setting文件
'''
#互亿无线短信配置
HY_MSM_URL='http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_MSM_PARAMS={
    'account':'C15238037',
    'password':'b69e39e8da612951795282cffb5774e0',
    'content':'您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile':'None',
    'format':'json'
}


# HY_MSM_URL='http://106.ihuyi.com/webservice/sms.php?method=Submit'
# HY_MSM_PARAMS={
#     'account':'C15238037',
#     'password':'b69e39e8da612951795282cffb5774e0',
#     'content':'您的验证码是：%s。请不要把验证码泄露给其他人。',
#     'mobile':'None',
#     'format':'json'
# }
# YZX_MSM_PARAMS={
#  "sid":"3785bab0dbeb5f94a436a9d45fedfd1f",
#  "token":"98fde1594515b9f04be25a7220f82ea0",
#  "appid":"4beecec84d4d47c3aa4fda4f14a2ef5f",
#  "templateid":"154501",
#  "param":"87828,3",
#  "mobile":"None",
#  "uid""2d92c6132139467b989d087c84a365d8",

# }

# import os
# from celery import Celery
#
# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')
#
# app = Celery('swiper')
#
# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('worker.config')
#
# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()



# def debug_task(func):
#     task_result=app.task(func)
#     return  task_result.delay()







