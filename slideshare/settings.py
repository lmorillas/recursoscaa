# -*- coding: utf-8 -*-

# Scrapy settings for slideshare project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'slideshare'

SPIDER_MODULES = ['slideshare.spiders']
NEWSPIDER_MODULE = 'slideshare.spiders'

HTTPCACHE_ENABLED = True
DOWNLOAD_DELAY = 0.50

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'slideshare (+http://www.yourdomain.com)'
