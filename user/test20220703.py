#
# import  time
# from celery import  Celery
#
# broker="redis://127.0.0.1:6379"
# backen="redis://127.0.0.1:6379/0"    #redis本身是16个数据库的，这个是选择第0个
# app=Celery("my_task",broker=broker,backend=backen)
#
# @app.task
# def add(x,y):
#     time.sleep(5)  #模拟耗时操作
#     return x+y
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
