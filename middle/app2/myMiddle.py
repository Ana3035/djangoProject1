from django.utils.deprecation import MiddlewareMixin
class MyMiddle(MiddlewareMixin):#表示了一个继承
    #此函数在发起请求之前执行
    def process_request(self,requests):
        print("get:",requests.GET.get('a'))#只能读不能修改