# -*- coding: utf-8 -*-
# @Time    : 18-2-28 下午7:59
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 04.compile.py
# @Software: PyCharm

# 函数re.compile将正则表达式（以字符串书写的）转换为模式对象，可以实现更加有效的匹配。例子：
import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
reg = re.findall(r'\w*oo\w*', text)    #查找所有包含'oo'的单词
print(reg)
regex = re.compile(r'\w*oo\w*')  # TODO 可以提高效率，返回正则对象，方便调用，不用总写一串正则表达式
print (regex.findall(text)) #查找所有包含’oo’的单词