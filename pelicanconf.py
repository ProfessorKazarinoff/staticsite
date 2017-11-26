#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter Kazarinoff'
SITENAME = 'Python Programming for Undergraduate Engineers'
SITEURL = ''
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images','extra','code','posts/seaborn_bar_plot_files']
PLUGIN_PATHS = ['pelican-plugins']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
	'extra/jupyter.css': {'path': 'static/css/jupyter.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
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

#Theme, environements and plugins
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
FAVICON = 'extra/favicon.ico'
AVATAR ='extra/gear-wrench-icon-512-278694.png'
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'
PYGMENTS_STYLE = 'native'

#to ignore any injected css for ipynb pages
IPYNB_IGNORE_CSS = True

#For voidy-bootstrap that allows first article full page
#THEME = 'pelican-themes/voidy-bootstrap'
#BOOTSTRAP_STYLESHEET ='bootstrap.flatly.min.css'
#ARTICLE_FULL_FIRST = True
#SIDEBAR = 'sidebar.html'


#Plugins, extensions
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = [
    'i18n_subsites','series','tag_cloud',
    'liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube',
    'liquid_tags.vimeo',
    'liquid_tags.include_code','liquid_tags.notebook',
    'render_math','tipue_search', 'pelican_javascript', 'pelican-bootstrapify',
    'pelican-ipynb.markup', 'pelican-ipynb.liquid']

NOTEBOOK_DIR = 'posts'

I18N_TEMPLATES_LANG = 'en'
MARKUP = ('md', 'ipynb')
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
		'markdown.extensions.tables': {},
    },
    'output_format': 'html5',
}
#Ignore all files that start with a dot .
IGNORE_FILES = ['.*','*-checkpoint.ipynb']

# URL's
#SLUGIFY_SOURCE = 'title'
#PAGE_URL = 'pages/{slug}/'
#ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#USE_PAGER = True
#BOOTSTRAP_FLUID = True

# Breadcrumbs
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

# Banner
#BANNER = '/path/to/banner.png'
#BANNER_SUBTITLE = 'This is my subtitle'
#BANNER_ALL_PAGES =  True

SERIES_TEXT = 'This article is the %(index)s of the %(name)s series'
#sidebar options
   # Tag Cloud Options
DISPLAY_SERIES_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 10
   # Recent Posts in Sidebas
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 3
   # Series infor on sidebar
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
#MENUITEMS = ['Home','About','Search']
ARCHIVES_SAVE_AS = 'archives.html'
DISPLAY_ARCHIVE_ON_MENU = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
ABOUT_ME = 'I teach engineering at a communtiy college in the Pacific Northwest. ' \
           'I am interested in programming and how to help students. ' \
           'Here I mostly blog about Python, MATLAB and how programing can be incorporated into engineering education.'
#AVATAR = 'images/about_me_image.png'

# for Tique Search Plugin
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5
