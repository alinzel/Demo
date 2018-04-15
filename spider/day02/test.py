# -*- coding: utf-8 -*-
# import urllib
# import urllib2
# import re
#
# #处理页面标签类
# class Tool:
#     removeImg = re.compile('<img.*?>| {7}|') #去除img标签,7位长空格
#     removeAddr = re.compile('<a.*?>|</a>') #删除超链接标签
#     replaceLine = re.compile('<tr>|<div>|</div>|</p>')   #把换行的标签换为\n
#     replaceTD= re.compile('<td>')  #将表格制表<td>替换为\t
#     replacePara = re.compile('<p.*?>') #把段落开头换为\n加空两格
#     replaceBR = re.compile('<br><br>|<br>') #将换行符或双换行符替换为\n
#     removeExtraTag = re.compile('<.*?>')#将其余标签剔除
#
#     def replace(self,x):
#         x = re.sub(self.removeImg,"",x)
#         x = re.sub(self.removeAddr,"",x)
#         x = re.sub(self.replaceLine,"\n",x)
#         x = re.sub(self.replaceTD,"\t",x)
#         x = re.sub(self.replacePara,"\n    ",x)
#         x = re.sub(self.replaceBR,"\n",x)
#         x = re.sub(self.removeExtraTag,"",x)
#         return x.strip()  #strip()将前后多余内容删除
#
#
# #百度贴吧爬虫类
# class BDTB:
#     #初始化，传入基地址，是否只看楼主的参数
#     def __init__(self,baseUrl,seeLZ,floorTag):
#         #base链接地址
#         self.baseURL = baseUrl
#         #是否只看楼主
#         self.seeLZ = '?see_lz='+str(seeLZ)
#         #HTML标签剔除工具类对象
#         self.tool = Tool()
#         #全局file变量，文件写入操作对象
#         self.file = None
#         #楼层标号，初始为1
#         self.floor = 1
#         #默认的标题，如果没有成功获取到标题的话则会用这个标题
#         self.defaultTitle = u"百度贴吧"
#         #是否写入楼分隔符的标记
#         self.floorTag = floorTag
#
#     #传入页码，获取该页帖子的代码
#     def getPage(self,pageNum):
#         try:
#             #构建URL
#             url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
#             request = urllib2.Request(url)
#             response = urllib2.urlopen(request)
#             #返回UTF-8格式编码内容
#             return response.read().decode('utf-8')
#         #无法连接，报错
#         except urllib2.URLError, e:
#             if hasattr(e,"reason"):
#                 print u"连接百度贴吧失败,错误原因",e.reason
#                 return None
#
#     #获取帖子标题
#     def getTitle(self,page):
#         #得到标题的正则表达式
#         pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
#         result = re.search(pattern,page)
#         if result:
#             #如果存在，则返回标题
#             return result.group(1).strip()
#         else:
#             return None
#
#     #获取帖子一共有多少页
#     def getPageNum(self,page):
#         #获取帖子页数的正则表达式
#         pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
#         result = re.search(pattern,page)
#         if result:
#             return result.group(1).strip()
#         else:
#             return None
#
#     #获取每一层楼的内容,传入页面内容
#     def getContent(self,page):
#         #匹配所有楼层的内容
#         pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
#         items = re.findall(pattern,page)
#         contents = []
#         for item in items:
#             #将文本进行去除标签处理，同时在前后加入换行符
#             content = "\n"+self.tool.replace(item)+"\n"
#             contents.append(content.encode('utf-8'))
#         return contents
#
#     def setFileTitle(self,title):
#         #如果标题不是为None，即成功获取到标题
#         if title is not None:
#             self.file = open(title + ".txt","w+")
#         else:
#             self.file = open(self.defaultTitle + ".txt","w+")
#
#     def writeData(self,contents):
#         #向文件写入每一楼的信息
#         for item in contents:
#             if self.floorTag == '1':
#                 #楼之间的分隔符
#                 floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
#                 self.file.write(floorLine)
#             self.file.write(item)
#             self.floor += 1
#
#     def start(self):
#         indexPage = self.getPage(1)
#         pageNum = self.getPageNum(indexPage)
#         title = self.getTitle(indexPage)
#         self.setFileTitle(title)
#         if pageNum == None:
#             print "URL已失效，请重试"
#             return
#         try:
#             print "该帖子共有" + str(pageNum) + "页"
#             for i in range(1,int(pageNum)+1):
#                 print "正在写入第" + str(i) + "页数据"
#                 page = self.getPage(i)
#                 contents = self.getContent(page)
#                 self.writeData(contents)
#         #出现写入异常
#         except IOError,e:
#             print "写入异常，原因" + e.message
#         finally:
#             print "写入任务完成"
#
#
# baseURL = 'https://tieba.baidu.com/p/' + str(raw_input("请输入帖子代号"))
# seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0\n")
# floorTag = raw_input("是否写入楼层信息，是输入1，否输入0\n")
# bdtb = BDTB(baseURL,seeLZ,floorTag)
# bdtb.start()

# from urllib import request
# url = 'https://tieba.baidu.com/p/5530143748/0/?pn=1'
#
# req = request.Request(url)
# resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))


# from urllib import request
# import re
#
#
# def zhengze(html):
#     author = re.findall(r'<i class="icon_author"></i>.*?<a rel="noreferrer".*?class="frs-author-name j_user_card " href=.*?target="_blank">(.*?)</a>', html, re.S)
#     title = re.findall(r'<a rel="noreferrer".*?title="(.*?)" target="_blank" class="j_th_tit ">.*?</a>',html)
#     # print(author,title)
#     file = open('bdtb.txt','w')
#     for i in range(0, len(author)):
#         file.write('作者:'+author[i]+'\n\r')
#         file.write('标题:'+title[i]+'\n\r')
#     file.close()
# def target_url():
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
#     }
#     url = 'https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=0'
#     html = request.Request(url, headers=header)
#     html = request.urlopen(html)
#     text = html.read().decode()
#     return text
# if __name__ == '__main__':
#     text = target_url()
#     zhengze(text)




# # #处理页面标签类
# class Tool:
#     removeImg = re.compile('<img.*?>| {7}|') #去除img标签,7位长空格
#     removeAddr = re.compile('<a.*?>|</a>') #删除超链接标签
#     replaceLine = re.compile('<tr>|<div>|</div>|</p>')   #把换行的标签换为\n
#     replaceTD= re.compile('<td>')  #将表格制表<td>替换为\t
#     replacePara = re.compile('<p.*?>') #把段落开头换为\n加空两格
#     replaceBR = re.compile('<br><br>|<br>') #将换行符或双换行符替换为\n
#     removeExtraTag = re.compile('<.*?>')#将其余标签剔除
#
#     def replace(self,x):
#         x = re.sub(self.removeImg,"",x)
#         x = re.sub(self.removeAddr,"",x)
#         x = re.sub(self.replaceLine,"\n",x)
#         x = re.sub(self.replaceTD,"\t",x)
#         x = re.sub(self.replacePara,"\n    ",x)
#         x = re.sub(self.replaceBR,"\n",x)
#         x = re.sub(self.removeExtraTag,"",x)
#         return x.strip()  #strip()将前后多余内容删除
#
#
# #百度贴吧爬虫类
# class BDTB:
#     #初始化，传入基地址，是否只看楼主的参数
#     def __init__(self,baseUrl,seeLZ,floorTag):
#         #base链接地址
#         self.baseURL = baseUrl
#         #是否只看楼主
#         self.seeLZ = '?see_lz='+str(seeLZ)
#         #HTML标签剔除工具类对象
#         self.tool = Tool()
#         #全局file变量，文件写入操作对象
#         self.file = None
#         #楼层标号，初始为1
#         self.floor = 1
#         #默认的标题，如果没有成功获取到标题的话则会用这个标题
#         self.defaultTitle = u"百度贴吧"
#         #是否写入楼分隔符的标记
#         self.floorTag = floorTag
#
#     #传入页码，获取该页帖子的代码
#     def getPage(self,pageNum):
#         try:
#             #构建URL
#             url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
#             req = request.Request(url)
#             response = request.urlopen(req)
#             #返回UTF-8格式编码内容
#             return response.read().decode('utf-8')
#         #无法连接，报错
#         except error.URLError as e:
#             if hasattr(e,"reason"):
#                 print ("连接百度贴吧失败,错误原因",e.reason)
#                 return None
#
#     #获取帖子标题
#     def getTitle(self,page):
#         #得到标题的正则表达式
#         pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
#         result = re.search(pattern,page)
#         if result:
#             #如果存在，则返回标题
#             return result.group(1).strip()
#         else:
#             return None
#
#     #获取帖子一共有多少页
#     def getPageNum(self,page):
#         #获取帖子页数的正则表达式
#         pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
#         result = re.search(pattern,page)
#         if result:
#             return result.group(1).strip()
#         else:
#             return None
#
#     #获取每一层楼的内容,传入页面内容
#     def getContent(self,page):
#         #匹配所有楼层的内容
#         pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
#         items = re.findall(pattern,page)
#         contents = []
#         for item in items:
#             #将文本进行去除标签处理，同时在前后加入换行符
#             content = "\n"+self.tool.replace(item)+"\n"
#             contents.append(content)
#         return contents
#
#     def setFileTitle(self,title):
#         #如果标题不是为None，即成功获取到标题
#         if title is not None:
#             self.file = open(title + ".txt","w+")
#         else:
#             self.file = open(self.defaultTitle + ".txt","w+")
#
#     def writeData(self,contents):
#         #向文件写入每一楼的信息
#         for item in contents:
#             if self.floorTag == '1':
#                 #楼之间的分隔符
#                 floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
#                 self.file.write(floorLine)
#             self.file.write(item)
#             self.floor += 1
#
#     def start(self):
#         indexPage = self.getPage(1)
#         pageNum = self.getPageNum(indexPage)
#         title = self.getTitle(indexPage)
#         self.setFileTitle(title)
#         if pageNum == None:
#             print ("URL已失效，请重试")
#             return
#         try:
#             print ("该帖子共有" + str(pageNum) + "页")
#             for i in range(1,int(pageNum)+1):
#                 print ("正在写入第" + str(i) + "页数据")
#                 page = self.getPage(i)
#                 contents = self.getContent(page)
#                 self.writeData(contents)
#         #出现写入异常
#         except IOError as e:
#             print ("写入异常，原因" + e.message)
#         finally:
#             print ("写入任务完成")
#
#
# baseURL = 'https://tieba.baidu.com/p/' + str(input("请输入帖子代号"))
# seeLZ = input("是否只获取楼主发言，是输入1，否输入0\n")
# floorTag = input("是否写入楼层信息，是输入1，否输入0\n")
# bdtb = BDTB(baseURL,seeLZ,floorTag)
# bdtb.start()

i = 'sdknfdsvn sdfdf'
a = i.split(' ')
print(i)