# -*- coding: utf-8 -*-
# @Time    : 18-2-28 下午6:57
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 03.bs4_test.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import requests

header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}
url = 'https://movie.douban.com/chart'
html = requests.get(url, headers=header)
print(type(html))  # TODO <class 'requests.models.Response'> 请求的响应类

# 创建beautifulsoup对象 TODO BeautifulSoup（抓取的源码，字符串形式，解析器类型）
html = BeautifulSoup(html.text, 'lxml')

# TODO Tag(标签)，返回第一个匹配的，而不是所有
# print(html.title)  # 得到标签 <title>豆瓣电影排行榜</title>
# print(html.name)  # TODO 返回文档类型
# print(html.title.name)   # TODO 返回标签类型
# print(html.a.attrs)  # TODO 打印当前标签所有的属性
# # TODO 获取对应标签的属性值，两种获取字典中value的值的方法【key】，get(key)
# print(html.a.attrs["href"])
# print(html.a.get("class"))
# print(html.prettify())  # TODO 格式化输出代码
#
# # TODO 标签中的内容-string，strings，stripped_strings
# print(html.title.string)  # TODO 打印当前标签中的文本内容
#
# string_s = html.title.strings   # TODO 返回生成器，获取当前标签下所有子标签下内容，包括换行符空格等
# for i in string_s:
# 	print(i)
#
# stripped_string_s = html.title.stripped_strings  # TODO 返回生成器，获取当前标签下所有子标签下内容，不包括换行符空格等
# print(stripped_string_s)
# for i in stripped_string_s:
# 	print(i)

a = '''
<html>
<body>
	<div>这是一个div
		<p>子孙节点p</p>
	</div>
	<span>span子节点</span>
</body>
</html>
'''
a = BeautifulSoup(a,'lxml')
# TODO 子节点(包括后代) .contents .children
# print(a.body.contents)  # TODO 返回列表，包括换行符，返回当前标签下的第一个子节点
# for i in a.body.children:  # TODO 返回生成器，遍历取出 ,不包含换行符等
# 	print(i)

# TODO 子孙节点--依次遍历每一个节点，并输出文本 .descendants
for i in a.body.descendants:  # TODO 返回生成器，第一个子节点（所有内容 + 文本）子节点的子节点知道没有了，进行下一个子节点（兄弟节点）
	print(i)
