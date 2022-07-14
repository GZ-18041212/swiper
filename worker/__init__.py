import  os
from  celery import  Celery
# from swiper import  settings

#加载环境变量，加载django的setting的
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')

#创建celery的application
celery_app=Celery('swiper')
celery_app.config_from_object('worker.config')   #这是可以从其他模块加载
# celery_app.autodiscover_tasks()    #自动发现运行任务
celery_app.autodiscover_tasks(['user.logic.send_vertify_code'])   #要把需要异步执行的任务放这里
# celery_app.autodiscover_tasks(['swiper.urls','swiper'])
# celery_app.autodiscover_tasks(['user'])    #自动发现运行任务

def call_by_worker(func):
    "将任务在celery中异步执行"
    task=celery_app.task(func)    #异步执行函数
    return task.delay     #返回上面异步执行结果的










