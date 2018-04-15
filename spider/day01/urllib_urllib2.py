# coding:utf-8
import urllib, urllib2

# # 定义请求网址
# url = 'http://www.baidu.com/'
#
# # urlopen(要打开的网址，要传入的数据.....)，返回文件对象
# # urlopen,是ssl请求，只能打开http请求，不能打开https请求
# resp = urllib.urlopen(url)
# # <addinfourl at 139870087262864 whose fp = <socket._fileobject object at 0x7f360cb3f9d0>>
# print resp
# # 查看源代码
# print resp.read()
# # 查看详细信息，
# print resp.info()
# # 查看状态码
# print resp.getcode()

# 解决urllib()不能请求https的问题
# url = 'https://www.zhihu.com/question/49144687'
# url = 'https://www.cnblogs.com/thrillerz/p/6464203.html'

# # 加入页面中的User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
# header = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
# # 'Referrer':'https://www.zhihu.com/question/49144687',
# }

# res = urllib2.Request(url, headers=header)
# resp = urllib2.urlopen(res)
# # resp = urllib.urlopen(url) # TODO 也可以请求https?
# print resp.read()

# 传参data并拼接URL
url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd='
data = { 'key': '红海行动'}
res = urllib.urlencode(data)
base_url = url + res
resp = urllib.urlopen(base_url)
print resp.read()


