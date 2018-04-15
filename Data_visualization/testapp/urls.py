from django.conf.urls import include, url
from . import views

urlpatterns = [
	# 首页的URL
    url(r'index/', views.index),
    # 请求JSON数据的URL
    url(r'^json_data/$', views.json_data)
]