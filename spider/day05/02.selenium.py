# -*- coding: utf-8 -*-
# @Time    : 18-3-1 下午2:21
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 02.selenium.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

# 创建驱动对象，打开谷歌webdriver
dirver = webdriver.Chrome()
try:
	# 设置隐式等待时间，TODO 监听上边代码，无论上边是否执行完成，都会等待，直到时间结束
	dirver.implicitly_wait(10)
	# 打开请求链接
	dirver.get('https:taobao.com')
	# TODO 设置显示等待时间----WebDriverWait(webdriver驱动, 时间秒)--》机制，每隔一段时间进行检查是否找到，找到就继续执行，不必等待时间结束
	# 代码解释： 查找元素，在等待时间内没有找到会抛出TimeOut错误
	input = WebDriverWait(dirver, 1).until(
		# 查找元素 TODO 等价input = dirver.find_element_by_id('q')
		EC.presence_of_element_located((By.ID, 'q'))
	)
	# 向查找的元素中传入数据
	input.send_keys('python')
	# 查找元素并设置点击事件
	dirver.find_element_by_class_name('search-button').click()
	# 打印源码
	print(dirver.page_source)
except TimeoutException as t:
	print('超时')
finally:
	# 关闭窗口
	dirver.quit()


