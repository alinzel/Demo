# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_introduce project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# TODO 根目录的名字
BOT_NAME = 'scrapy_introduce'
# TODO scrapy默认搜索spider列表，默认【】
SPIDER_MODULES = ['scrapy_introduce.spiders']
# TODO 使用genspider命令创建新的spider模块，默认‘’
NEWSPIDER_MODULE = 'scrapy_introduce.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_introduce (+http://www.yourdomain.com)'

# Obey robots.txt rules
# TODO 是否遵守robot协议，默认True,改为False
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# TODO scrapy并发请求链接的最大值，默认16
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# TODO 下载器下载同一个网站的下一页前需要等待的时间。默认0，支持小数
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# TODO 对单个网站并发请求的最大值
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# TODO 对单个IP并发请求的最大值
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# TODO cookie默认不可用？
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TODO Telent终端是否可用
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# TODO scrapy默认的请求头信息
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# TODO 爬虫的中间件 ，当修改中间件后需要激活，数字小，权重大，先执行
#SPIDER_MIDDLEWARES = {
#    'scrapy_introduce.middlewares.ScrapyIntroduceSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# TODO 下载器中间件
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_introduce.middlewares.ScrapyIntroduceDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# TODO 保存项目中启用插件顺序的字典
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# TODO 管道
#ITEM_PIPELINES = {
#    'scrapy_introduce.pipelines.ScrapyIntroducePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
