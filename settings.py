# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'

MONGO_URI='localhost'
MONGO_DATABASE='zhihu'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36',
    'cookie': '_zap=2f8ef279-e80f-45eb-9fd3-ade83bfecc40; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1581252714,1581252744,1581252771,1581252803; d_c0="ABCYUILkpBCPTnASYbLkNoQdsVe9hQHR3to=|1578723662"; _xsrf=ERMWVOwb2rVQs58ntZrPfPcsJE2sY6rY; capsion_ticket="2|1:0|10:1581253632|14:capsion_ticket|44:NjZkYzIwZWRmMTQxNGFiNzhkZGYzOGEyMWMxMjA5OTk=|a6d2476c17e6ab5f12a762b1d991f7be72e00c32f056d2e2932db82c9af37956"; tst=f; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1581253648|1581252802; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1581253628; q_c1=c42ad3a11e544feeb25481159c6c6728|1581252837000|1581252837000; z_c0="2|1:0|10:1581253648|4:z_c0|92:Mi4xeDlRc0JBQUFBQUFBRUpoUWd1U2tFQ1lBQUFCZ0FsVk5FRkl0WHdENkRkdGZ0ajJ2TGJhY19ucEdjMkVSUTNXNG1R|622302b7762cc78d27e0b87d637a59e1d613466b52c8a71a90f2448d8d40d249'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihu.pipelines.ZhihuPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline':301
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#调度器

SCHEDULER="scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS="scrapy_redis.dupefilter.RFPDupeFilter"
REDIS_URL="redis://hc:longhuan@127.0.0.1:"