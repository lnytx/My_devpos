"""My_devpos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from cmdb import views as cmdb_views
from devmanage import views as devmanage_views
from login import views as login_views


urlpatterns = [
    url(r'^aaa/$',login_views.aaa),
    url(r'^admin/', admin.site.urls),
    url(r'^base/', login_views.aaa),
    url(r'^ajax_dict/', login_views.ajax_dict),
    url(r'^ajax_list/', login_views.ajax_list),
    url(r'^$',login_views.index),
    url(r'^index/$',login_views.index),
    url(r'^login/$',login_views.login),
    url(r'^logout/$',login_views.logout),
    url(r'^accounts/login',login_views.index),
    url(r'^dev_manage/$',devmanage_views.dev_view),
    url(r'^ip_manage/$',devmanage_views.ip_view),
    url(r'^add_ip/$',devmanage_views.add_ip),
    url(r'^add_dev/$',devmanage_views.add_dev),
    url(r'^search_ip/$',devmanage_views.search_ip),
    url(r'^search_dev/$',devmanage_views.search_dev),
    url(r'^mod_ip/$',devmanage_views.mod_ip),
    url(r'^mod_dev/$',devmanage_views.mod_dev),
]
