#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter Kazarinoff'
SITENAME = 'Python for Undergraduate Engineers'
SITEURL = ''
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images','extra','code',
                'posts/seaborn_bar_plot_files',
                'posts/micropython',
                'posts/micropython/images',
                'extra/CNAME',
                'extra/.nojekyll',
                'code/circuit_diagrams',
                'code/flask',
                'code/sympy',
                'code/statistics',
                'code/matplotlib_plots/stress_strain_curves/images'
                'posts/jupyter',
                'posts/jupyter/images',
                'posts/jupyterhub',
                'posts/fairtalk'
                'posts/matplotlib/images',
                'posts/matplotlib',
                'posts/matplotlib_animations/images',
                'posts/resources/images',
                'posts/schemdraw',
                'posts/transfer_app/images',
                'posts/arduino/images',
                'posts/django/images',
                'posts/pswp_book/images',
                'posts/git/images',
                'posts/podcast/images',
                'posts/functions/images',
                'posts/django_iot_server/images',
                'posts/flask',
                'posts/pypdx_west/images',
                'posts/pswp_book/images',
                'posts/pdf/images',
                'posts/engr213/images',
                'posts/ansible/images',
                'posts/streamlit/images',
                'posts/jupyterhub_2020Q1/images',
                'posts/top_five/images',
                'posts/zappa/images',
                'posts/zappa/images/aws',
                'posts/voila/images',
                'posts/testing_science_code/images',
                'posts/stream/images',
                'posts/email/images',
                'posts/tesseract/images',
                'pages/gear/images',
                'posts/engr231/images',
                'posts/math/images',
                'posts/numpy/images',
                ]
                
PLUGIN_PATHS = ['pelican-plugins','extra-plugins']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/jupyter.css': {'path': 'static/css/jupyter.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'},
    'extra/nojekyll': {'path': '.nojekyll'},
    'extra/CNAME': {'path': 'CNAME'},
}
#consider above to have extra/custom.js bath go to static/theme/js and see if that works

SUMMARY_MAX_LENGTH = 50
WITH_FUTURE_DATES = False
# default status to draft (pages not published) unless Status: published is spelled out in the .md post
#DEFAULT_METADATA = {
#    'JavaScripts': 'table.js',
#    'Stylesheets': 'table.css'
#    'status': 'draft',
#}

# Theme, environements and plugins
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
FAVICON = 'extra/favicon.ico'
AVATAR ='extra/gear-wrench-icon-512-278694.png'
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'
PYGMENTS_STYLE = 'native'
THEME_TEMPLATES_OVERRIDES = ['theme-overrides']

#to ignore any injected css for ipynb pages
IPYNB_IGNORE_CSS = True  ###change back!!!!!!!!!!!!!
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

#For voidy-bootstrap that allows first article full page
#THEME = 'pelican-themes/voidy-bootstrap'
#BOOTSTRAP_STYLESHEET ='bootstrap.flatly.min.css'
#ARTICLE_FULL_FIRST = True
#SIDEBAR = 'sidebar.html'


#Plugins, extensions
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.img',
    'liquid_tags.video',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.vimeo',
    'liquid_tags.include_code',
    'pelican_javascript',
    'related_posts',
    'render_math',
    'tipue_search',
    'pelican-ipynb.markup',
    'neighbors',
    'bootswatch_markdown_css',
    ] # 'pelican_javascript', 'pelican-bootstrapify'


NOTEBOOK_DIR = 'posts'

I18N_TEMPLATES_LANG = 'en'
MARKUP = ('md', 'ipynb', 'html')
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {'title': 'Table of contents:'}, #consider out
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
	    'markdown.extensions.tables': {},
        'markdown.extensions.admonition': {},
        'pymdownx.smartsymbols': {},
    },
    'output_format': 'html5',
}

# could not get 'pymdownx.superfences': {}, to work.

# Ignore all files that start with a dot .
IGNORE_FILES = ['.*','*-checkpoint.ipynb','app.ipynb']

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

# URL's
#DRAFT_URL = 'drafts/{slug}.html'
#DRAFT_SAVE_AS = 'drafts/{slug}.html'
#SLUGIFY_SOURCE = 'title'
#PAGE_URL = 'pages/{slug}/'
#ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#USE_PAGER = True
BOOTSTRAP_FLUID = True

# Breadcrumbs
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

# Banner
#BANNER = '/path/to/banner.png'
#BANNER_SUBTITLE = 'This is my subtitle'
#BANNER_ALL_PAGES =  True

SERIES_TEXT = 'Article %(index)s of the %(name)s series'
# Sidebar options
   # Tag Cloud Options
DISPLAY_SERIES_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 10
   # Recent posts in side bar
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 3
   # Series info on sidebar
SHOW_SERIES = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
    #Github on sidebar
GITHUB_USER = 'professorkazarinoff'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Top menus
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
# MENUITEMS = ['Home','About','Search']
ARCHIVES_SAVE_AS = 'archives.html'
DISPLAY_ARCHIVE_ON_MENU = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
ABOUT_ME = 'I teach engineering at a community college in the Pacific Northwest. ' \
           'I am interested in programming and how to help students. ' \
           'Here I mostly blog about Python, and how programing can be incorporated into engineering education.'
# AVATAR = 'images/about_me_image.png'

# for Tique Search Plugin
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# for Google Analytics
GOOGLE_ANALYTICS = 'UA-116330557-1'

# Add This (tweet, like, email buttons on posts)
ADDTHIS_PROFILE = "ra-5cdd8eb4e16bf94c"
ADDTHIS_DATA_TRACK_ADDRESSBAR = False
ADDTHIS_FACEBOOK_LIKE = True
ADDTHIS_TWEET = True
ADDTHIS_EMAIL = True
ADDTHIS_GOOGLE_PLUSONE = False

# Ethical Adds in Sidebar
ETHICAL_ADS = True

DEFAULT_PAGINATION = 5
