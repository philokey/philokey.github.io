#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'philokey'
SITENAME = u'philokey\u7684\u7b14\u8bb0'
SITEURL = 'http://www.philokey.com'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

#THEME = 'bootstrap'

THEME = 'tuxlite_tbs'
DISQUS_SITENAME = 'philokeygithubio'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

GOOGLE_ANALYTICS = 'UA-53439918-1'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'



#plugins

#PLUGIN_PATH = u"/usr/local/lib/python2.7/site-packages/pelican/pelican-plugins"
PLUGIN_PATHS= u"/Users/philokey/Practice/github/pelican-plugins"
PLUGINS = ['sitemap','render_math']

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Google', 'https://www.google.com/ncr'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/philokey'),
		  (u'微博', 'http://weibo.com/u/1690959514/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing

RELATIVE_URLS = True

ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'


