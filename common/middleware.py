# from logging import getLogger
# from traceback import  format_exc
#
from django.http import  HttpResponse
from django.utils.deprecation import   MiddlewareMixin

class Corsmiddleware(MiddlewareMixin):
    #处理客户端js的跨域
    def proccess_request(self,request):
        if request.method=='OPTIONS' and 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response=HttpResponse()
            response['Content-Lenth']='0'
            response['Access-Control-Allow-Headers']=request.META
            ['HTTP_ACCESS_CONTROL_REQUEST_METHOD']
            response['Access-Control-Allow-Origin']='http://127.0.0.1:8000'
            return  response
    def proccess_response(self,request,response):
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
        response['Access-Control-Allow-Credentials']='true'
        return response











