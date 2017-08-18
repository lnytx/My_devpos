# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from devmanage.pymysql_conn import delete_table, select_table, \
    select_all, insert_table, update_table


#from My_devpos.devmanage.pymysql_conn.py import select_table, insert_table
each_page=3

@login_required
def ip_view(request):
    '''show ip list'''
    #del ip前台点击删除时发送的ip到后台,逐条删除
    if request.method =='POST':
        ip=request.POST.getlist('post_ip')
        for i in ip:
            #p=select_table('host',i)
            delete_table('host',i)
    #然后查询整个表，显示所有数据
    ip_list=select_all('host')
    paginator=Paginator(ip_list,each_page)
    page=request.GET.get('page',1)
    try:
        show_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_list = paginator.page(1)
    except (EmptyPage,InvalidPage):
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_list = paginator.page(paginator.num_pages)
    return render_to_response('ip_manage.html',{'username':request.user.username,'show_list':show_list,'ip_list':ip_list,'paginator':paginator})

@login_required
def dev_view(request):
    '''show dev list'''
    #如果是查询时
    if request.method =='POST':
        ip=request.POST.getlist('post_ip')
        for i in ip:
            p=select_table('device_status',i)
            delete_table('device_status', p)

    #show  Paginator分页显示
    dev_list=select_all('device_status')
    paginator=Paginator(dev_list,each_page)
    page=request.GET.get('page',1)

    try:
        show_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_list = paginator.page(1)
    except (EmptyPage,InvalidPage):
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_list = paginator.page(paginator.num_pages)
    dev_list=select_all('device_status')
    return render_to_response('dev_manage.html',{'username':request.user.username,'show_list':show_list,'paginator':paginator})

@login_required
def add_ip(request):
    '''add ip'''
    if request.method == 'POST':
        ip=request.POST.get('ipaddr')
        if len(select_table('host', ip)) != 0:
            return render_to_response('add_ip.html',{'username':request.user.username,'add_error':'IP已经存在!'})
        else:
            data={
                'ip':request.POST.get('ipaddr'),
                'hostname':request.POST.get('hostname'),
                'ostype':request.POST.get('ostype'),
                'ports':request.POST.get('ports'),
                'application':request.POST.get('application'),
                'pwd':request.POST.get('passwd','root'),
                'username':request.POST.get('username','root'),
                }
            print("data",data)
            insert_table('host', data)


    return render_to_response('add_ip.html',{'username':request.user.username})

@login_required
def add_dev(request):
    '''add dev'''
    if request.method =='POST':
        ip=request.POST.get('ipaddr')
        if len(select_table('device_status', ip)) != 0:
            return render_to_response('add_dev.html',{'username':request.user.username,'add_error':'IP已经存在!'})
        else:
            data={
                'ipaddr':request.POST.get('ipaddr'),
                'cpu':request.POST.get('cpu'),
                'memory':request.POST.get('memory'),
                'location':request.POST.get('location'),
                'product':request.POST.get('product'),
                'platform':request.POST.get('platform'),
                'sn':request.POST.get('sn'),
                }
            insert_table('device_status', data)

    return render_to_response('add_dev.html',{'username':request.user.username})


@login_required
def search_ip(request):
    '''search ip list'''
    if 'search' in request.GET and request.GET.get('search'):
        s_text=request.GET.get('search').strip()
        print("search",s_text)
        if len(s_text) != 0:
            #还没有做orm
            ip_list=select_table('host', s_text)
            print("ip_list",ip_list)
            if len(ip_list) == 0:
                return render_to_response('ip_manage.html',{'username':request.user.username,'search_error':'查找内容不存在！'})

        paginator=Paginator(ip_list,each_page)
        page=request.GET.get('page',1)
        try:
            show_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_list = paginator.page(1)
        except (EmptyPage,InvalidPage):
            # If page is out of range, deliver last page of results.
            show_list = paginator.page(paginator.num_pages)
        return render_to_response('ip_manage.html',{'username':request.user.username,'show_list':show_list,'paginator':paginator,'s_text':s_text})

@login_required
def search_dev(request):
    '''search dev list'''
    if 'search' in request.GET and request.GET.get('search'):
        s_text=request.GET.get('search').strip()
        if len(s_text) != 0:
            ip_list=select_table('device_status', s_text)
            if len(ip_list) == 0:
                return render_to_response('dev_manage.html',{'username':request.user.username,'search_error':'查找内容不存在！'})

        paginator=Paginator(ip_list,each_page)
        page=request.GET.get('page',1)
        try:
            show_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_list = paginator.page(1)
        except (EmptyPage,InvalidPage):
            # If page is out of range, deliver last page of results.
            show_list = paginator.page(paginator.num_pages)
        return render_to_response('dev_manage.html',{'username':request.user.username,'show_list':show_list,'paginator':paginator,'s_text':s_text})

@login_required
#查看对应IP主机的详细信息，这里接收传自前台的IP地址
def mod_ip(request):
    if 'ip' in request.GET:
        ip=request.GET.get('ip')
        ip_info=select_table('host', ip)

    if request.method =='POST':
        ip=request.GET.get('ip')
        data={
            'ip':ip,
            'hostname':request.POST.get('hostname'),
            'ostype':request.POST.get('ostype'),
            'ports':request.POST.get('ports'),
            'application':request.POST.get('application'),
            'username':request.POST.get('username'),
            'pwd':request.POST.get('passwd'),
            }
        print("data",data)
        update_table('host',data)


    return render_to_response('add_ip.html',{'username':request.user.username,'ip_info':ip_info})



@login_required
def mod_dev(request):
    if 'ip' in request.GET:
        ip=request.GET.get('ip')
        dev_info=select_table('device_status', ip)

    if request.method =='POST':
        ip=request.GET.get('ip')
        data={
            'ip':ip,
            'cpu':request.POST.get('cpu'),
            'memory':request.POST.get('memory'),
            'location':request.POST.get('location'),
            'product':request.POST.get('product'),
            'platform':request.POST.get('platform'),
            'sn':request.POST.get('sn'),
            }
        update_table('device_status',data)
    return render_to_response('add_dev.html',{'username':request.user.username,'dev_info':dev_info})




