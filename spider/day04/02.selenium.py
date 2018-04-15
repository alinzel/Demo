# -*- coding: utf-8 -*-
# @Time    : 18-3-1 下午2:21
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 02.selenium.py
# @Software: PyCharm
from selenium import webdriver


# 创建驱动对象，打开谷歌webdriver
dirver = webdriver.Chrome()
# 打开请求链接
html = dirver.get('https:taobao.com')
# 查找元素
input = dirver.find_element_by_id('q')
# 向查找的元素中传入数据
input.send_keys('python')
# 查找元素并设置点击事件
dirver.find_element_by_class_name('search-button').click()
# 打印源码
print(dirver.page_source)
# 关闭窗口
dirver.quit()


