#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://pythonforundergradengineers.com'
RELATIVE_URLS = True

# RSS Feed Settings
FEED_DOMAIN = SITEURL
FEED_ATOM = None
FEED_RSS = 'rss'
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = True

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
# for Google Analytics
GOOGLE_ANALYTICS = 'UA-116330557-1'
