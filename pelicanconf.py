#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import datetime

AUTHOR = 'tatomoaki'
SITENAME = 'tatomoaki'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = 'en'


SITETITLE = 'Tato Moaki'
SITESUBTITLE = 'Full Stack Software Engineer'
SITEDESCRIPTION = 'python, AWS, Django, Flask, Angular'
SITELOGO = '/images/me.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/tatomoaki/'),
        ('twitter', 'http://twitter.com/tatomoaki'),
        ('github', 'http://github.com/tatomoaki'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/Users/tato/pelican-themes/Flex'
COPYRIGHT_YEAR = datetime.now().year