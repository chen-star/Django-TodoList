from django.conf.urls import url
from django.contrib import admin
from todolist import views
from . import views

urlpatterns = [

    # 分配一个叫作 index 的 view 到 ^$ 的 URL 上
    # 正则表达会会匹配 ^（表示开头）并紧随 $ （表示结尾），所以只有空字符串会被匹配到
    # name='index' 是 URL 的名字，用来唯一标识对应的 view
    url(r'^$', views.todolist, name = 'index'),
    url(r'^admin/', admin.site.urls),
    url(r'^delete/(?P<pk>\d+)/', views.delete),
    url(r'^complete/(?P<pk>\d+)/', views.complete),
]