# coding:utf-8
# @Time    : 18-2-27 下午6:06
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 08.百度贴吧.py
# @Software: PyCharm

from urllib import request, error
import re

# 处理页面标签类
class Tool(object):
	# TODO | 匹配|两边任意，从左边开始匹配，匹配到，则跳过右边
	# 去除img标签，7位长空格
	removeImg = re.compile(r'<img.*?>| {7}|')
	# 删除超链接标签
	removeAddr = re.compile(r'<a.*?>|</a>')
	# 把换行的标签转换\n
	replaceLine = re.compile(r'<tr>|<div>|</div>|</tr>')
	# 将制表符<td>转化成\t
	replaceTD = re.compile(r'<td>')
	# 把段落开头换位\n加空两个
	replacePara = re.compile(r'<p.*?>')
	# 将换行符或双换行符替换为\n
	replaceBR= re.compile(r'<br><br>|<br>')
	# 将其余标签都删除
	removeExteaTag = re.compile(r'<.*?>')

	def replace(self,x):
		x = re.sub(self.removeImg, '', x)
		x = re.sub(self.removeAddr, '', x)
		x = re.sub(self.replaceLine, '\n', x)
		x = re.sub(self.replaceTD, '\t', x)
		x = re.sub(self.replacePara, '\n  ', x)
		x = re.sub(self.replaceBR, '\n', x)
		x = re.sub(self.removeExteaTag, '', x)

		# strip()前后多余内容删除 TODO 返回替换后的结果
		return x.strip()


# 百度贴吧爬虫类
class BDTB(object):
	# 初始化，传入基础URL，是否只看楼主,显示楼层的参数
	def __init__(self, baseUrl, seeLZ, floorTag):
		# base链接地址
		self.baseUrl = baseUrl
		# 是否只看楼主
		self.seeLZ = '?see_lz=' + str(seeLZ)
		# 是否写入楼层分隔符的标记
		self.floorTag = floorTag
		# HTML标签剔除工具类 TODO 实例化一个类，类似于代理模式
		self.tool = Tool()
		# 全局file变量，文件写入操作对象
		self.file = None
		# 文件默认的标题，如果没有成功获取到标题，会用自定义的标题
		self.defaultTitle = u'百度贴吧'
		# 初始化写入的楼层
		self.floor = 1


	# 传入页码，获取该页帖子的代码
	def getPage(self, pageNum):
		try:
			# 构建URL url='https://tieba.baidu.com/p/5530143748/0/'
			url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
			print(url)
			# 请求链接
			req = request.Request(url)
			resp = request.urlopen(req)
			# 返回utf-8格式编码的内容 TODO 不decode以b''字节形式显示
			# print(resp.read().decode('utf-8'))
			return resp.read().decode('utf-8')
		# 无法链接，捕获错误
		except error.URLError as e:
			if hasattr(e,'reason'):
				print('链接百度贴吧失败，错误原因', e.reason)
				return None


	# 获取帖子标题 TODO page?
	def getTitle(self,page):
		# 得到标题的正则表达式
		pattern = re.compile(r'<h3 class="core_title_txt pull-left text-overflow".*?>'
							 r'(.*?)</h3>', re.S)
		result = re.search(pattern,page)
		if result:
			# 返回标题
			return result.group(1).strip()
		else:
			return None


	# 获取帖子一共多少页
	def getPageNum(self,page):
		# 获取帖子页数的正则表达式
		# pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
		pattern = re.compile(r'<li class="l_reply_num".*?</span>.*?<span class="red">(.*?)</span>',re.S)
		result = re.search(pattern,page)
		print(result)
		if result:
			return result.group(1).strip()
		else:
			return None


	# 获取每一层页面的内容，传入页面内容
	def getContent(self, page):
		# 匹配所有楼层的内容
		pattern = re.compile(r'<div id=".*?" class="d_post_content j_d_post_content ">'
							 r'(.*?)</div>', re.S)
		items = re.findall(pattern,page)
		contents = []
		for item in items:
			# 将文本进行去除标签处理，同时在前后加上换行符
			content = '\n'+self.tool.replace(item)+'\n'
			contents.append(content.encode('utf-8'))
		return contents


	# 设置文件标题
	def setFileTitle(self,title):
		if title is not None:
			self.file = open(title+ ".txt", 'w+')
		else:
			self.file = open(self.defaultTitle + '.txt', 'w+')


	# 向文件中写入信息
	def writeDate(self,contents):
		# 向文件写入每一楼的数据
		for item in contents:
			if self.floorTag == '1':
				# 楼层间的分隔符
				floorLine = '\n' + str(self.floor) +"-----------------------------------------------------------------------------------------\n"
				self.file.write(floorLine)
			self.file.write(item)
			self.floor +=1


	# TODO 主程序入口
	def start(self):
		indexPage = self.getPage(1)
		# print(indexPage)
		pageNum = self.getPageNum(indexPage)
		title = self.getTitle(indexPage)
		self.setFileTitle(title)
		if pageNum == None:
			print('URL已失效，请重试')
			return
		try:
			print('该帖子共有' + str(pageNum) + '页')
			for i in range(1,int(pageNum)+1):
				print('正在写入第%s页数据' % str(i))
				page = self.getPage(i)
				contents = self.getContent(page)
				self.writeDate(contents)
		# 出现写入异常
		except IOError as e:
			print('写入异常，原因' + e.message)
		finally:
			print('写入任务完成')

baseUrl = 'https://tieba.baidu.com/p/'+ input('请输入帖子代号：')
seeLZ = input('是否只获取楼主发言，是=1，否=0：')
floorTag = input('是否写入楼层信息，是=1，否=0：')
bdtb = BDTB(baseUrl, seeLZ, floorTag)
bdtb.start()