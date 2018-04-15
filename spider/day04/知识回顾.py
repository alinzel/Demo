# -*- coding: utf-8 -*-
# @Time    : 18-3-1 下午4:34
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 知识回顾.py
# @Software: PyCharm

a = []
b = [1,2,3,4,]
for i in b:
	if i%2==0:
		a.append(i)
print(a)

a = []
b = (x for x in range(1,5))
for i in b:
	if i%2==0:
		a.append(i)
print(a)