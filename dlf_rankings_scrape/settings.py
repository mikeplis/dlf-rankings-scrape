# -*- coding: utf-8 -*-

# Scrapy settings for dlf_rankings_scrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dlf_rankings_scrape'

SPIDER_MODULES = ['dlf_rankings_scrape.spiders']
NEWSPIDER_MODULE = 'dlf_rankings_scrape.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
