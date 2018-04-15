# -*- coding: utf-8 -*-
# @Time    : 18-2-28 上午11:39
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 01.session_模拟登陆.py
# @Software: PyCharm

import requests
import re
'''
模拟登录
	正常登录，构建符合条件的数据，登录成功后拿着session访问登陆成功后可以查看的页面
'''

# TODO GET请求页面
# url = 'http://apply.tjjttk.gov.cn/apply/person/login.html?r=0.5702432438718941'
url = 'http://www.tjjttk.gov.cn/'
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}
page = requests.get(url,headers=header ).text
print(page)

# TODO 获取验证码
# 对page进行解码
reg = re.compile(r'<td.*?id="grGetValidCodeImg">.*?<img src="(.*?)">')
result = re.search(reg, page)
print(result)
