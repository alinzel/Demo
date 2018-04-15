# -*- coding: utf-8 -*-
# @Time    : 18-2-26 下午7:36
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 01.urllib.py
# @Software: PyCharm
import urllib

# 定义一个URL
url = 'http://www.baidu.com'

# urlopen(请求网址，参数data)
# TODO urllib下的urlopen为ssl协议请求，有些https协议不能直接请求，要用到urllib2的request
# resp = urllib.urlopen(url)
# print resp  # 返回文件类型对象
# print resp.read()  #查看源代码
# print resp.info()  # 打印详细信息
# print resp.getcode()  # 打印响应状态码


# TODO 请求网址参数有中文会自动转化为十六进制？
# url1 = 'http://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=url%20uri%20%E5%8C%BA%E5%88%AB&oq=%25E4%25B8%2580%25E4%25B8%25AA%25E4%25B8%25AD%25E6%2596%2587%25E5%25AD%2597%25E7%25AC%25A6%25E5%258D%25A0%25E5%2587%25A0%25E4%25B8%25AA%25E5%25AD%2597%25E8%258A%2582&rsv_pq=87024e30000248a0&rsv_t=949f7y3tZCtulRrg3Ik4CyZn9feo2bLfnmVSqse%2BxWfqiJn9mKRXI6VXV4M&rqlang=cn&rsv_enter=1&inputT=7560&rsv_sug3=30&rsv_sug1=21&rsv_sug7=100&rsv_sug2=1&prefixsug=URL%2520uri&rsp=0&rsv_sug4=7560'
url1 = 'http://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=红海行动&oq=url%2520uri%2520%25E5%258C%25BA%25E5%2588%25AB&rsv_pq=cdc5fd190003333b&rsv_t=409a7Yc8TnHemR3P4xdfH99w4IQ8sROA%2BIzF%2Fa5FC4V8waHrQNr3Ms5vi28&rqlang=cn&rsv_enter=0&inputT=1360&rsv_sug3=31&rsv_sug1=22&rsv_sug7=100&prefixsug=%25E5%258C%25BA%25E5%2588%25AB&rsp=0&rsv_sug4=1361'

# resp1 = urllib.urlopen(url1)
# print resp1
# print resp1.read()


# url拼接参数data,urlencode({key:value})
# TODO urllib中传入data,不会改变请求方式 ，没有get_method()
data = {
	'key':'捉妖记2'
}

url2 = 'http://www.baidu.com'
req = urllib.urlencode(data)
base_url = 'http://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=' + req
resp2 = urllib.urlopen(base_url)

print resp2.read()
