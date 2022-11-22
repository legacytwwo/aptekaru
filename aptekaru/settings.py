BOT_NAME = 'aptekaru'

SPIDER_MODULES = ['aptekaru.spiders']
NEWSPIDER_MODULE = 'aptekaru.spiders'

#USER_AGENT = 'aptekaru (+http://www.yourdomain.com)'

# LOG_LEVEL = 'ERROR'
ROBOTSTXT_OBEY = False
FEED_EXPORT_ENCODING = 'utf-8'
# DOWNLOAD_TIMEOUT = 15
# RETRY_ENABLED = True
# RETRY_TIMES = 8
# RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408]
# DOWNLOAD_DELAY = 0.25

#CONCURRENT_REQUESTS = 32

#DOWNLOAD_DELAY = 3
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

#COOKIES_ENABLED = False

#TELNETCONSOLE_ENABLED = False

#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

#SPIDER_MIDDLEWARES = {
#    'aptekaru.middlewares.AptekaruSpiderMiddleware': 543,
#}

# DOWNLOADER_MIDDLEWARES = {
#    'aptekaru.middlewares.CustomProxyMiddleware': 350,
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
# }

#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

#ITEM_PIPELINES = {
#    'aptekaru.pipelines.AptekaruPipeline': 300,
#}

#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#AUTOTHROTTLE_DEBUG = False

#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
