# -*- coding: utf-8 -*-
import json
from logging import root

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.messages.storage import session
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response


#直接无modles在Mysql数据库中生成Django默认的auth_user等表
#采用了django的auth系统
def aaa(request):
    return render_to_response('lianxi.html')

def ajax_list(request):
    a = [1,2,3,4,5,6]
    return HttpResponse(json.dumps(a), content_type='application/json')
 
def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')



# Create your views here.
def index(request):
    '''判断用户是否登陆'''
    #.is_authenticated()通过判断session中是否有user_id 以及user_backend 来判断用户是否登陆。
    if not  request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username=request.user.username
    return render_to_response('ip_manage.html',{'username':username})

def login(request):
    '''
    2.插入数据用户名密码时应该用User.objects.create_user(username=username,password=password)，这个方法会把密码生成哈希值，插进数据库，而不能用User.objects.create（。。。。），这样插进去的数据密码是明文滴~~~~

                总结：用对方法User.objects.create_user(username=username,password=password)，插对表user
    '''
    #User.objects.create_user(username='root',password='root')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username is not None and password is not None:
            user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            #request.session['username']=username
            return HttpResponseRedirect('/index/')
        else:
            return render_to_response('login.html',{'login_error':'用户名或密码错误!'})
    return render_to_response('login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')