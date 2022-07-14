# BROKER_URL = 'redis://127.0.0.1:6379/0'
broker_url = 'redis://127.0.0.1:6379'     #0704修改过
broker_pool_limit = 1000   #broker连接池，默认是10

timezone = 'Asia/Shanghai'
accept_content=['pickle','json']

task_serializer='pickle'

# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# result_backend_url='redis://127.0.0.1:6379/0'    #0704修改过
result_backend ='redis://127.0.0.1:6379/0'    #0704修改过
result_serializer='json'
result_cache_max=10000    #缓任务结果最大缓存
result_expires=3600   #任务结果的过期时间

worker_redirect_stdouts_level='INFO'





