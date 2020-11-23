from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.
"""
视图
所谓的视图就是Python函数
视图函数有两个要求:
    1.视图函数的第一个参数就是接受请求.
    这个请求就是 HttpRequest 的类对象
    2.必须返回一个响应
"""
def index(request):
    return HttpResponse('ok!')