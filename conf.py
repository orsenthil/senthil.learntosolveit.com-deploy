# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time
import os

BLOG_AUTHOR = "Senthil Kumaran"
BLOG_TITLE = "Senthil Kumaran"
SITE_URL = "http://senthil.learntosolveit.com/"

BLOG_EMAIL = "orsenthil@gmail.com"
BLOG_DESCRIPTION = ""  # (translatable)

DEFAULT_LANG = "en"

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/index.html', 'Home', 'fa fa-home'),
        ('/archive.html', 'Archives', 'fa fa-folder-open'),
        ('/categories/index.html', 'Tags', 'fa fa-tags'),
        ('/rss.xml', 'RSS', 'fa fa-rss'),
        ('https://twitter.com/phoe6', 'My Twitter', 'fa fa-twitter'),
        ('https://github.com/orsenthil', 'My Github', 'fa fa-github'),
    )
}

DATE_FANCINESS = 2


# Name of the theme to use.
THEME = "zen-forkawesome"

# Primary color of your theme. This will be used to customize your theme and
# auto-generate related colors in POSTS_SECTION_COLORS. Must be a HEX value.
THEME_COLOR = '#5670d4'

POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.md", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
)

PAGES = (
    ("stories/*.rst", "stories", "story.tmpl"),
    ("stories/*.txt", "stories", "story.tmpl"),
    ("stories/*.md", "stories", "story.tmpl"),
    ("stories/*.html", "stories", "story.tmpl"),
)

#  Add the orgmode compiler to your COMPILERS dict.
#COMPILERS["orgmode"] = ('.org',)

# Add org files to your POSTS, PAGES
# POSTS = POSTS + (("posts/*.org", "posts", "post.tmpl"),)
# PAGES = PAGES + (("stories/*.org", "stories", "story.tmpl"),)

# Below this point, everything is optional

# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (e.g. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use the ISO 8601/RFC 3339 format (ex. 2012-03-30T23:00:00+02:00)
TIMEZONE = "US/Pacific"

# If you want to use ISO 8601 (also valid RFC 3339) throughout Nikola
# (especially in new_post), set this to True.
# Note that this does not affect DATE_FORMAT.
# FORCE_ISO8601 = False

# Date format used to display post dates. (translatable)
# (str used by datetime.datetime.strftime)
# DATE_FORMAT = '%Y-%m-%d %H:%M'

# Date format used to display post dates, if local dates are used. (translatable)
# (str used by moment.js)
# JS_DATE_FORMAT = 'YYYY-MM-DD HH:mm'

# Use date-based path when creating posts?
# Can be enabled on a per-post basis with `nikola new_post -d`.
# The setting is ignored when creating pages.
NEW_POST_DATE_PATH = True

# What format to use when creating posts with date paths?
# Default is '%Y/%m/%d', other possibilities include '%Y' or '%Y/%m'.

NEW_POST_DATE_PATH_FORMAT = '%Y/%m/%d'

# Date fanciness.
#
# 0 = using DATE_FORMAT and TIMEZONE
# 1 = using JS_DATE_FORMAT and local user time (via moment.js)
# 2 = using a string like “2 days ago”
#
# Your theme must support it, bootstrap and bootstrap3 already do.
# DATE_FANCINESS = 0

# While Nikola can select a sensible locale for each language,
# sometimes explicit control can come handy.
# In this file we express locales in the string form that
# python's locales will accept in your OS, by example
# "en_US.utf8" in Unix-like OS, "English_United States" in Windows.
# LOCALES = dict mapping language --> explicit locale for the languages
# in TRANSLATIONS. You can omit one or more keys.
# LOCALE_FALLBACK = locale to use when an explicit locale is unavailable
# LOCALE_DEFAULT = locale to use for languages not mentioned in LOCALES; if
# not set the default Nikola mapping is used.

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of {source: relative destination}.
# Default is:
# FILES_FOLDERS = {'files': ''}
# Which means copy 'files' into 'output'

# One or more folders containing listings to be processed and stored into
# the output. The format is a dictionary of {source: relative destination}.
# Default is:
# LISTINGS_FOLDERS = {'listings': 'listings'}
# Which means process listings from 'listings' into 'output/listings'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is HTML and just copies it

COMPILERS = {
    "rest": ('.txt', '.rst'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "html": ('.html', '.htm'),
}

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# If this is set to True, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# If this is set to False, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# Formerly known as HIDE_UNTRANSLATED_POSTS (inverse)
# SHOW_UNTRANSLATED_POSTS = True

# Nikola supports logo display.  If you have one, you can put the URL here.
# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
# LOGO_URL = 'https://dl.dropboxusercontent.com/s/1iewg2le17sf0pq/xtoinfinity_300_100.png'
#LOGO_URL = 'http://dl.dropbox.com/s/bd3ghra88e765q5/xtoinfinity_300_100.svg'
# LOGO_URL = 'https://dl.dropboxusercontent.com/s/9wfngl1x5h25309/xtoinfinity-logo2.png'

# If you want to hide the title of your website (for example, if your logo
# already contains the text), set this to False.
SHOW_BLOG_TITLE = True

# Writes tag cloud data in form of tag_cloud_data.json.
# Warning: this option will change its default value to False in v8!
WRITE_TAG_CLOUD = True

# Generate pages for each section. The site must have at least two sections
# for this option to take effect. It wouldn't build for just one section.
# POSTS_SECTIONS = True

# Setting this to False generates a list page instead of an index. Indexes
# are the default and will apply GENERATE_ATOM if set.
# POSTS_SECTIONS_ARE_INDEXES = True

# Each post and section page will have an associated color that can be used
# to style them with a recognizable color detail across your site. A color
# is assigned to  each section based on shifting the hue of your THEME_COLOR
# at least 7.5 % while leaving the lightness and saturation untouched in the
# HUSL colorspace. You can overwrite colors by assigning them colors in HEX.
# POSTS_SECTION_COLORS = {
#     DEFAULT_LANG: {
#         'posts':  '#49b11bf',
#         'reviews':   '#ffe200',
#     },
# }

# Associate a description with a section. For use in meta description on
# section index pages or elsewhere in themes.
# POSTS_SECTION_DESCRIPTIONS = {
#     DEFAULT_LANG: {
#         'how-to': 'Learn how-to things properly with these amazing tutorials.',
#     },
# }

# Sections are determined by their output directory as set in POSTS by default,
# but can alternatively be determined from file metadata instead.
# POSTS_SECTION_FROM_META = False

# Names are determined from the output directory name automatically or the
# metadata label. Unless overwritten below, names will use title cased and
# hyphens replaced by spaces.
# POSTS_SECTION_NAME = {
#    DEFAULT_LANG: {
#        'posts': 'Blog Posts',
#        'uncategorized': 'Odds and Ends',
#    },
# }

# Titles for per-section index pages. Can be either one string where "{name}"
# is substituted or the POSTS_SECTION_NAME, or a dict of sections. Note
# that the INDEX_PAGES option is also applied to section page titles.
# POSTS_SECTION_TITLE = {
#     DEFAULT_LANG: {
#         'how-to': 'How-to and Tutorials',
#     },
# }

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
 # (translatable)
# TAG_PATH = "categories"

# See TAG_PATH's "list of tags" for the default setting value. Can be overwritten
# here any path relative to the output directory.
 # (translatable)
# TAGS_INDEX_PATH = "tags.html"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = False

# Set descriptions for tag pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the tag list or index page’s title.
# TAG_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for tag pages. The default is "Posts about TAG".
# TAG_PAGES_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a tag publicly, you can mark it as hidden.
# The tag will not be displayed on the tag list page, the tag cloud and posts.
# Tag pages will still be generated.
HIDDEN_TAGS = ['mathjax']

# Only include tags on the tag list/overview page if there are at least
# TAGLIST_MINIMUM_POSTS number of posts or more with every tag. Every tag
# page is still generated, linked from posts, and included in the sitemap.
# However, more obscure tags can be hidden from the tag index page.
# TAGLIST_MINIMUM_POSTS = 1

# Final locations are:
# output / TRANSLATION[lang] / CATEGORY_PATH / index.html (list of categories)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category.html (list of posts for a category)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category.xml (RSS feed for a category)
# (translatable)
# CATEGORY_PATH = "categories"
# CATEGORY_PREFIX = "cat_"

# If CATEGORY_ALLOW_HIERARCHIES is set to True, categories can be organized in
# hierarchies. For a post, the whole path in the hierarchy must be specified,
# using a forward slash ('/') to separate paths. Use a backslash ('\') to escape
# a forward slash or a backslash (i.e. '\//\\' is a path specifying the
# subcategory called '\' of the top-level category called '/').
CATEGORY_ALLOW_HIERARCHIES = True
# If CATEGORY_OUTPUT_FLAT_HIERARCHY is set to True, the output written to output
# contains only the name of the leaf category and not the whole path.
CATEGORY_OUTPUT_FLAT_HIERARCHY = True

# If CATEGORY_PAGES_ARE_INDEXES is set to True, each category's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# CATEGORY_PAGES_ARE_INDEXES = False

# Set descriptions for category pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the category list or index page’s title.
# CATEGORY_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for category pages. The default is "Posts about CATEGORY".
# CATEGORY_PAGES_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a category publicly, you can mark it as hidden.
# The category will not be displayed on the category list page.
# Category pages will still be generated.
HIDDEN_CATEGORIES = []

# If ENABLE_AUTHOR_PAGES is set to True and there is more than one
# author, author pages are generated.
# ENABLE_AUTHOR_PAGES = True

# Final locations are:
# output / TRANSLATION[lang] / AUTHOR_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / AUTHOR_PATH / author.html (list of posts for a tag)
# output / TRANSLATION[lang] / AUTHOR_PATH / author.xml (RSS feed for a tag)
# AUTHOR_PATH = "authors"

# If AUTHOR_PAGES_ARE_INDEXES is set to True, each author's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# AUTHOR_PAGES_ARE_INDEXES = False

# Set descriptions for author pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the author list or index page’s title.
# AUTHOR_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "Juanjo Conti": "Python coder and writer.",
#        "Roberto Alsina": "Nikola father."
#    },
# }


# If you do not want to display an author publicly, you can mark it as hidden.
# The author will not be displayed on the author list page and posts.
# Tag pages will still be generated.
HIDDEN_AUTHORS = ['Guest']

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# INDEX_PATH = ""

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
# CREATE_SINGLE_ARCHIVE = False
# Create year, month, and day archives each with a (long) list of posts
# (overrides both CREATE_MONTHLY_ARCHIVE and CREATE_SINGLE_ARCHIVE)
# CREATE_FULL_ARCHIVES = False
# If monthly archives or full archives are created, adds also one archive per day
# CREATE_DAILY_ARCHIVE = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / DAY / index.html
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# If ARCHIVES_ARE_INDEXES is set to True, each archive page which contains a list
# of posts will contain the posts themselves. If set to False, it will be just a
# list of links.
# ARCHIVES_ARE_INDEXES = False

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# If USE_BASE_TAG is True, then all HTML files will include
# something like <base href=http://foo.var.com/baz/bat> to help
# the browser resolve relative links.
# In some rare cases, this will be a problem, and you can
# disable it by setting USE_BASE_TAG to False.
# USE_BASE_TAG = True

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Slug the Tag URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# Slug the Author URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_AUTHOR_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [["2007/02/28/lost-and-found/index.html", "/posts/2007/02/28/lost-and-found.html"], ["2014/06/26/started-with-the-tower/index.html", "/posts/2014/06/26/started-with-the-tower.html"], ["2004/10/11/a-good-quote/index.html", "/posts/2004/10/11/a-good-quote.html"], ["2013/01/26/vishwaroopam-and-grave-dangers-ahead-for-the-society/index.html", "/posts/2013/01/26/vishwaroopam-and-grave-dangers-ahead-for-the-society.html"], ["2011/05/09/happy-mothers-day-commerce/index.html", "/posts/2011/05/09/happy-mothers-day-commerce.html"], ["2007/02/22/recent-books/index.html", "/posts/2007/02/22/recent-books.html"], ["2004/07/12/next-foldoc-entry-lilo/index.html", "/posts/2004/07/12/next-foldoc-entry-lilo.html"], ["2014/08/29/madurai-meenakshi-temple-in-minecraft-2/index.html", "/posts/2014/08/29/madurai-meenakshi-temple-in-minecraft-2.html"], ["2014/07/21/temple-with-pond/index.html", "/posts/2014/07/21/temple-with-pond.html"], ["2006/01/26/photos-of-my-home-town/index.html", "/posts/2006/01/26/photos-of-my-home-town.html"], ["2003/12/26/alice-vs-alan/index.html", "/posts/2003/12/26/alice-vs-alan.html"], ["2007/09/13/karate-photos-yellow-to-orange-belt-graduation-day/index.html", "/posts/2007/09/13/karate-photos-yellow-to-orange-belt-graduation-day.html"], ["2007/01/08/the-adventures-of-tintin/index.html", "/posts/2007/01/08/the-adventures-of-tintin.html"], ["2014/06/23/madurai-meenakshi-temple-in-minecraft-day-1/index.html", "/posts/2014/06/23/madurai-meenakshi-temple-in-minecraft-day-1.html"], ["2010/11/25/good-quote-10/index.html", "/posts/2010/11/25/good-quote-10.html"], ["2013/09/27/1344/index.html", "/posts/2013/09/27/1344.html"], ["2007/03/09/eclipsed-moon/index.html", "/posts/2007/03/09/eclipsed-moon.html"], ["2011/04/30/order-to-read-asimovs-robot-and-empire-series/index.html", "/posts/2011/04/30/order-to-read-asimovs-robot-and-empire-series.html"], ["2004/11/28/weekends/index.html", "/posts/2004/11/28/weekends.html"], ["2007/03/02/marvin-minsky-on-ai/index.html", "/posts/2007/03/02/marvin-minsky-on-ai.html"], ["2008/12/07/funny-trick-using-your-gmail-id/index.html", "/posts/2008/12/07/funny-trick-using-your-gmail-id.html"], ["2011/10/06/heres-to-the-crazy-one/index.html", "/posts/2011/10/06/heres-to-the-crazy-one.html"], ["2006/11/10/ssk-participation-in-jack-kilby-quiz/index.html", "/posts/2006/11/10/ssk-participation-in-jack-kilby-quiz.html"], ["2009/12/27/chief-programmer/index.html", "/posts/2009/12/27/chief-programmer.html"], ["2004/07/16/on-becoming-an-expert-c-programmer/index.html", "/posts/2004/07/16/on-becoming-an-expert-c-programmer.html"], ["2008/10/29/captain-haddocks-curses/index.html", "/posts/2008/10/29/captain-haddocks-curses.html"], ["2005/10/14/gnometintin/index.html", "/posts/2005/10/14/gnometintin.html"], ["2014/02/11/codex-leicester/index.html", "/posts/2014/02/11/codex-leicester.html"], ["2006/11/13/quote-of-the-day/index.html", "/posts/2006/11/13/quote-of-the-day.html"], ["2005/08/22/why-didnt-they-ask-evans/index.html", "/posts/2005/08/22/why-didnt-they-ask-evans.html"], ["2006/03/14/happy-pi-day/index.html", "/posts/2006/03/14/happy-pi-day.html"], ["2007/02/16/how-love-works/index.html", "/posts/2007/02/16/how-love-works.html"], ["2007/10/09/slashdot-party-at-madurai/index.html", "/posts/2007/10/09/slashdot-party-at-madurai.html"], ["2013/03/04/my-birthday-treasure-hunt/index.html", "/posts/2013/03/04/my-birthday-treasure-hunt.html"], ["2013/12/29/interactive-programming-in-python/index.html", "/posts/2013/12/29/interactive-programming-in-python.html"], ["2004/01/25/with-rms-the-guru-of-gnu/index.html", "/posts/2004/01/25/with-rms-the-guru-of-gnu.html"], ["2008/02/08/maharishi-mahesh-yogi-passes-away/index.html", "/posts/2008/02/08/maharishi-mahesh-yogi-passes-away.html"], ["2004/07/02/finishing-work-quickly/index.html", "/posts/2004/07/02/finishing-work-quickly.html"], ["2014/06/27/madurai-meenakshi-temple-in-minecraft-north-tower-under-constructin/index.html", "/posts/2014/06/27/madurai-meenakshi-temple-in-minecraft-north-tower-under-constructin.html"], ["2009/01/11/of-sourashtra-speaking-people/index.html", "/posts/2009/01/11/of-sourashtra-speaking-people.html"], ["2009/09/28/brainfuck/index.html", "/posts/2009/09/28/brainfuck.html"], ["2010/07/13/good-quote-8/index.html", "/posts/2010/07/13/good-quote-8.html"], ["2005/03/17/1111111111/index.html", "/posts/2005/03/17/1111111111.html"], ["2009/10/09/pells-equation/index.html", "/posts/2009/10/09/pells-equation.html"], ["2012/10/12/shavarsh-karapetyan/index.html", "/posts/2012/10/12/shavarsh-karapetyan.html"], ["2015/05/23/positive-thinking/index.html", "/posts/2015/05/23/positive-thinking.html"], ["2015/07/30/greatest-in-history-according-to-h-g-wells/index.html", "/posts/2015/07/30/greatest-in-history-according-to-h-g-wells.html"], ["2009/03/26/quotes/index.html", "/posts/2009/03/26/quotes.html"], ["2013/03/05/planning/index.html", "/posts/2013/03/05/planning.html"], ["2007/02/25/lisp-notes-1/index.html", "/posts/2007/02/25/lisp-notes-1.html"], ["2005/09/03/libsmbios/index.html", "/posts/2005/09/03/libsmbios.html"], ["2014/06/30/temple-in-minecraft-day-7/index.html", "/posts/2014/06/30/temple-in-minecraft-day-7.html"], ["2004/09/15/the-software-developer/index.html", "/posts/2004/09/15/the-software-developer.html"], ["2007/04/23/vimplugin-for-eclipse/index.html", "/posts/2007/04/23/vimplugin-for-eclipse.html"], ["2010/06/16/canary-in-a-coalmine/index.html", "/posts/2010/06/16/canary-in-a-coalmine.html"], ["2007/03/10/ngwallpaper/index.html", "/posts/2007/03/10/ngwallpaper.html"], ["2010/06/15/py3k-peps-at-apac-pycon/index.html", "/posts/2010/06/15/py3k-peps-at-apac-pycon.html"], ["2008/12/18/discussing-english-grammar-in-the-bug-report/index.html", "/posts/2008/12/18/discussing-english-grammar-in-the-bug-report.html"], ["2005/05/28/forming-a-habit/index.html", "/posts/2005/05/28/forming-a-habit.html"], ["2005/01/09/finished-reading-five-point-someone/index.html", "/posts/2005/01/09/finished-reading-five-point-someone.html"], ["2009/01/16/good-quote-3/index.html", "/posts/2009/01/16/good-quote-3.html"], ["2015/05/20/1547/index.html", "/posts/2015/05/20/1547.html"], ["2008/08/30/robby-the-weight-lifter-from-india/index.html", "/posts/2008/08/30/robby-the-weight-lifter-from-india.html"], ["2006/09/17/vaishnavis-marriage-snaps/index.html", "/posts/2006/09/17/vaishnavis-marriage-snaps.html"], ["2012/10/02/happy-gandhi-jayanti-2/index.html", "/posts/2012/10/02/happy-gandhi-jayanti-2.html"], ["2004/10/08/linus-on-management/index.html", "/posts/2004/10/08/linus-on-management.html"], ["2010/06/05/fail-quickly/index.html", "/posts/2010/06/05/fail-quickly.html"], ["2007/03/29/pcl-syntax-and-semantics/index.html", "/posts/2007/03/29/pcl-syntax-and-semantics.html"], ["2015/11/21/computer-science-story-bottom-up/index.html", "/posts/2015/11/21/computer-science-story-bottom-up.html"], ["2009/06/19/muhammad-al-khowarizmi/index.html", "/posts/2009/06/19/muhammad-al-khowarizmi.html"], ["2014/12/04/cost-of-ideas-and-learning/index.html", "/posts/2014/12/04/cost-of-ideas-and-learning.html"], ["2008/09/19/discussion-on-all-or-nothing-approach/index.html", "/posts/2008/09/19/discussion-on-all-or-nothing-approach.html"], ["2008/10/24/bogosort/index.html", "/posts/2008/10/24/bogosort.html"], ["2009/12/09/wikipedia-forever/index.html", "/posts/2009/12/09/wikipedia-forever.html"], ["2005/08/31/steve-waugh/index.html", "/posts/2005/08/31/steve-waugh.html"], ["2008/10/18/all-science-is-either/index.html", "/posts/2008/10/18/all-science-is-either.html"], ["2011/10/02/happy-gandhi-jayanti/index.html", "/posts/2011/10/02/happy-gandhi-jayanti.html"], ["2004/09/27/a-quote-2/index.html", "/posts/2004/09/27/a-quote-2.html"], ["2005/01/19/it-was-five-past-midnight-2nd-to-3rd-december-1984-bhopal/index.html", "/posts/2005/01/19/it-was-five-past-midnight-2nd-to-3rd-december-1984-bhopal.html"], ["2007/09/18/watched-the-chronicles-of-narnia/index.html", "/posts/2007/09/18/watched-the-chronicles-of-narnia.html"], ["2015/05/26/galactic-league-of-civilizations/index.html", "/posts/2015/05/26/galactic-league-of-civilizations.html"], ["2008/03/19/godspeed-arthur-c-clarke/index.html", "/posts/2008/03/19/godspeed-arthur-c-clarke.html"], ["2005/06/26/maheswata/index.html", "/posts/2005/06/26/maheswata.html"], ["2013/11/24/correct-statement-and-truth/index.html", "/posts/2013/11/24/correct-statement-and-truth.html"], ["2013/11/09/ideas-books-flight/index.html", "/posts/2013/11/09/ideas-books-flight.html"], ["2007/01/30/remembering-mahatma/index.html", "/posts/2007/01/30/remembering-mahatma.html"], ["2015/05/31/elon-musk/index.html", "/posts/2015/05/31/elon-musk.html"], ["2007/03/08/happy-international-womens-day/index.html", "/posts/2007/03/08/happy-international-womens-day.html"], ["2011/07/07/freedom/index.html", "/posts/2011/07/07/freedom.html"], ["2004/06/01/irobot/index.html", "/posts/2004/06/01/irobot.html"], ["2007/05/29/random-c-stuff/index.html", "/posts/2007/05/29/random-c-stuff.html"], ["2013/07/08/my-three-wishes-for-minecraft/index.html", "/posts/2013/07/08/my-three-wishes-for-minecraft.html"], ["2007/03/10/science-of-god/index.html", "/posts/2007/03/10/science-of-god.html"], ["2005/06/23/genesis/index.html", "/posts/2005/06/23/genesis.html"], ["2007/03/22/pcl-a-practical-database/index.html", "/posts/2007/03/22/pcl-a-practical-database.html"], ["2008/12/23/once-in-a-blue-moon/index.html", "/posts/2008/12/23/once-in-a-blue-moon.html"], ["2007/06/28/m-x-viper-mode/index.html", "/posts/2007/06/28/m-x-viper-mode.html"], ["2012/01/30/remembering-mahatma-3/index.html", "/posts/2012/01/30/remembering-mahatma-3.html"], ["2007/04/11/norvig-on-spell-corrector/index.html", "/posts/2007/04/11/norvig-on-spell-corrector.html"], ["2007/05/28/n-puzzle-problem-solver-using-python/index.html", "/posts/2007/05/28/n-puzzle-problem-solver-using-python.html"], ["2013/03/02/1118/index.html", "/posts/2013/03/02/1118.html"], ["2007/10/11/photos-ahoy/index.html", "/posts/2007/10/11/photos-ahoy.html"], ["2013/07/01/computer-science-jobs-till-2020/index.html", "/posts/2013/07/01/computer-science-jobs-till-2020.html"], ["2007/03/26/soc-proposal-clean-up-urllib-in-python/index.html", "/posts/2007/03/26/soc-proposal-clean-up-urllib-in-python.html"], ["2007/06/22/yet-another-ubuntu-fan/index.html", "/posts/2007/06/22/yet-another-ubuntu-fan.html"], ["2006/10/08/finished-reading-the-hobbit/index.html", "/posts/2006/10/08/finished-reading-the-hobbit.html"], ["2007/03/03/ai-class-notes-2/index.html", "/posts/2007/03/03/ai-class-notes-2.html"], ["2007/07/14/programming-related-thought/index.html", "/posts/2007/07/14/programming-related-thought.html"], ["2015/06/01/1562/index.html", "/posts/2015/06/01/1562.html"], ["2012/11/16/stackoverflow-10000/index.html", "/posts/2012/11/16/stackoverflow-10000.html"], ["2009/10/01/8-bit-byte/index.html", "/posts/2009/10/01/8-bit-byte.html"], ["2015/07/19/papanasam/index.html", "/posts/2015/07/19/papanasam.html"], ["2005/01/12/the-right-to-read/index.html", "/posts/2005/01/12/the-right-to-read.html"], ["2009/01/01/just-wait-a-second/index.html", "/posts/2009/01/01/just-wait-a-second.html"], ["2013/09/11/how-to-get-better-at-programming/index.html", "/posts/2013/09/11/how-to-get-better-at-programming.html"], ["2013/07/14/amar-bose-1929-2013/index.html", "/posts/2013/07/14/amar-bose-1929-2013.html"], ["2013/09/11/to-change-the-world/index.html", "/posts/2013/09/11/to-change-the-world.html"], ["2012/01/09/magic-square-of-my-birthday/index.html", "/posts/2012/01/09/magic-square-of-my-birthday.html"], ["2010/10/02/gandhis-talisman/index.html", "/posts/2010/10/02/gandhis-talisman.html"], ["2008/06/12/good-will-hunting/index.html", "/posts/2008/06/12/good-will-hunting.html"], ["2004/04/07/foldoc-entry-to-editclause/index.html", "/posts/2004/04/07/foldoc-entry-to-editclause.html"], ["2009/01/01/happy-new-year-2009/index.html", "/posts/2009/01/01/happy-new-year-2009.html"], ["2007/05/03/peter-lunblad/index.html", "/posts/2007/05/03/peter-lunblad.html"], ["2013/07/17/idea-to-business-stages-involved/index.html", "/posts/2013/07/17/idea-to-business-stages-involved.html"], ["2009/09/29/surprising/index.html", "/posts/2009/09/29/surprising.html"], ["2008/12/05/tips-for-coping-with-disasters-rebt/index.html", "/posts/2008/12/05/tips-for-coping-with-disasters-rebt.html"], ["2007/07/06/shivaji/index.html", "/posts/2007/07/06/shivaji.html"], ["2015/06/10/on-goal-setting/index.html", "/posts/2015/06/10/on-goal-setting.html"], ["2007/01/18/men-who-made-new-physics/index.html", "/posts/2007/01/18/men-who-made-new-physics.html"], ["2012/10/23/an-evening-with-matz/index.html", "/posts/2012/10/23/an-evening-with-matz.html"], ["2003/11/03/software-should-be-simple/index.html", "/posts/2003/11/03/software-should-be-simple.html"], ["2015/06/02/algorithms-and-their-timeline/index.html", "/posts/2015/06/02/algorithms-and-their-timeline.html"], ["2006/12/19/neenas-marriage-cochin-trip-and-bannerghatta-np-visit/index.html", "/posts/2006/12/19/neenas-marriage-cochin-trip-and-bannerghatta-np-visit.html"], ["2009/01/16/good-quote-2/index.html", "/posts/2009/01/16/good-quote-2.html"], ["2006/09/03/whitespace-programming-language/index.html", "/posts/2006/09/03/whitespace-programming-language.html"], ["2007/01/01/happy-new-year/index.html", "/posts/2007/01/01/happy-new-year.html"], ["2003/12/26/why-john-smith/index.html", "/posts/2003/12/26/why-john-smith.html"], ["2011/09/11/a-call-within-a-call/index.html", "/posts/2011/09/11/a-call-within-a-call.html"], ["2007/01/29/fun-quote-and-guru-movie/index.html", "/posts/2007/01/29/fun-quote-and-guru-movie.html"], ["2013/06/26/why-do-some-people-like-programming/index.html", "/posts/2013/06/26/why-do-some-people-like-programming.html"], ["2014/06/28/minecraft-tower-in-shapse/index.html", "/posts/2014/06/28/minecraft-tower-in-shapse.html"], ["2005/11/27/rapple-1-0-release/index.html", "/posts/2005/11/27/rapple-1-0-release.html"], ["2013/03/13/we-are-sorry-to-inform-you/index.html", "/posts/2013/03/13/we-are-sorry-to-inform-you.html"], ["2009/10/21/python-strings-as-comments/index.html", "/posts/2009/10/21/python-strings-as-comments.html"], ["2004/06/28/fwd-re-foldoc-entry-to-edit-charles-t-marie-josephson-device-i-e-josephson-junction/index.html", "/posts/2004/06/28/fwd-re-foldoc-entry-to-edit-charles-t-marie-josephson-device-i-e-josephson-junction.html"], ["2014/06/24/meenakshi-temple-day-3-progress/index.html", "/posts/2014/06/24/meenakshi-temple-day-3-progress.html"], ["2013/05/19/if-a-thing-is/index.html", "/posts/2013/05/19/if-a-thing-is.html"], ["2008/12/23/hard-work-and-practice-in-programming/index.html", "/posts/2008/12/23/hard-work-and-practice-in-programming.html"], ["2013/06/16/30-years-of-kr-is-being-celebrated-this-is/index.html", "/posts/2013/06/16/30-years-of-kr-is-being-celebrated-this-is.html"], ["2015/05/26/john-muir/index.html", "/posts/2015/05/26/john-muir.html"], ["2005/03/18/captured-unix-time-1111111111/index.html", "/posts/2005/03/18/captured-unix-time-1111111111.html"], ["2007/04/17/using-ptags-py-for-tag-file/index.html", "/posts/2007/04/17/using-ptags-py-for-tag-file.html"], ["2007/09/05/teachers-day/index.html", "/posts/2007/09/05/teachers-day.html"], ["2011/07/02/inspiration/index.html", "/posts/2011/07/02/inspiration.html"], ["2014/07/07/tower-with-walls-on-side/index.html", "/posts/2014/07/07/tower-with-walls-on-side.html"], ["2004/06/28/josephson-junction/index.html", "/posts/2004/06/28/josephson-junction.html"], ["2013/06/09/the-incredibles-1/index.html", "/posts/2013/06/09/the-incredibles-1.html"], ["2008/01/08/quote-of-the-day-4/index.html", "/posts/2008/01/08/quote-of-the-day-4.html"], ["2010/10/09/the-pleasures-and-sorrows-of-work-amazon-book-link/index.html", "/posts/2010/10/09/the-pleasures-and-sorrows-of-work-amazon-book-link.html"], ["2006/12/08/scrmabled/index.html", "/posts/2006/12/08/scrmabled.html"], ["2014/06/25/looking-for-ideas-for-the-tower/index.html", "/posts/2014/06/25/looking-for-ideas-for-the-tower.html"], ["2007/03/05/lisp-notes-2-on-repl/index.html", "/posts/2007/03/05/lisp-notes-2-on-repl.html"], ["2008/06/21/about-ramanujan/index.html", "/posts/2008/06/21/about-ramanujan.html"], ["2003/12/08/foldoc-guest-editor/index.html", "/posts/2003/12/08/foldoc-guest-editor.html"], ["2007/09/16/guido-and-bruce-eckel-discuss-python-3000/index.html", "/posts/2007/09/16/guido-and-bruce-eckel-discuss-python-3000.html"], ["2008/01/15/robbie-the-ebot/index.html", "/posts/2008/01/15/robbie-the-ebot.html"], ["2007/04/25/a-xo-for-11-year-old-nigerian-students/index.html", "/posts/2007/04/25/a-xo-for-11-year-old-nigerian-students.html"], ["2007/01/13/movie-review-happy-feet/index.html", "/posts/2007/01/13/movie-review-happy-feet.html"], ["2012/02/05/small-aim-is-a-crime/index.html", "/posts/2012/02/05/small-aim-is-a-crime.html"], ["2013/05/15/bill-gates-reading-bed-time-story/index.html", "/posts/2013/05/15/bill-gates-reading-bed-time-story.html"], ["2013/12/19/data-structure-visualizations/index.html", "/posts/2013/12/19/data-structure-visualizations.html"], ["2004/04/07/fourth-generation-language/index.html", "/posts/2004/04/07/fourth-generation-language.html"], ["2007/02/22/shvedova-vs-santangelo/index.html", "/posts/2007/02/22/shvedova-vs-santangelo.html"], ["2014/05/31/irrationality-of-%e2%88%9a2/index.html", "/posts/2014/05/31/irrationality-of-a2.html"], ["2009/05/08/prisoners-dilemma/index.html", "/posts/2009/05/08/prisoners-dilemma.html"], ["2008/06/16/good-quote/index.html", "/posts/2008/06/16/good-quote.html"], ["2007/01/13/happy-feet-from-ssk/index.html", "/posts/2007/01/13/happy-feet-from-ssk.html"], ["2005/09/02/cprogramming-com-now-has-uthcode-as-a-resource/index.html", "/posts/2005/09/02/cprogramming-com-now-has-uthcode-as-a-resource.html"], ["2013/07/01/technology-devices-shipped-per-year-from-1975-to-2011/index.html", "/posts/2013/07/01/technology-devices-shipped-per-year-from-1975-to-2011.html"], ["2004/11/02/power-solutions-article/index.html", "/posts/2004/11/02/power-solutions-article.html"], ["2008/09/24/ariane-5-flight-501/index.html", "/posts/2008/09/24/ariane-5-flight-501.html"], ["2004/09/20/a-quote/index.html", "/posts/2004/09/20/a-quote.html"], ["2013/11/15/on-the-topic-of-good-work/index.html", "/posts/2013/11/15/on-the-topic-of-good-work.html"], ["2015/05/30/edsger-w-dijkstra/index.html", "/posts/2015/05/30/edsger-w-dijkstra.html"], ["2011/12/29/2011-in-science/index.html", "/posts/2011/12/29/2011-in-science.html"], ["2007/05/27/coding-and-karate/index.html", "/posts/2007/05/27/coding-and-karate.html"], ["2011/07/28/try/index.html", "/posts/2011/07/28/try.html"], ["2010/12/22/limits-of-the-possible/index.html", "/posts/2010/12/22/limits-of-the-possible.html"], ["2007/05/03/free-speech-flag/index.html", "/posts/2007/05/03/free-speech-flag.html"], ["2013/10/07/what-is-the-best-way-to-learn-a-new-programming-language/index.html", "/posts/2013/10/07/what-is-the-best-way-to-learn-a-new-programming-language.html"], ["2004/05/15/clause-foldoc-entry/index.html", "/posts/2004/05/15/clause-foldoc-entry.html"], ["2013/04/15/self-education-quote/index.html", "/posts/2013/04/15/self-education-quote.html"], ["2007/06/19/why-settle-for/index.html", "/posts/2007/06/19/why-settle-for.html"], ["2012/02/21/letter-to-a-teacher/index.html", "/posts/2012/02/21/letter-to-a-teacher.html"], ["2008/05/29/how-identation-works-for-python-programs/index.html", "/posts/2008/05/29/how-identation-works-for-python-programs.html"], ["2004/07/24/vaishnavi-got-placed-at-futuresoft/index.html", "/posts/2004/07/24/vaishnavi-got-placed-at-futuresoft.html"], ["2006/09/20/python-2-5-is-released/index.html", "/posts/2006/09/20/python-2-5-is-released.html"], ["2015/07/14/review-page-a-minute-memory-book/index.html", "/posts/2015/07/14/review-page-a-minute-memory-book.html"], ["2008/01/30/remembering-mahatma-2/index.html", "/posts/2008/01/30/remembering-mahatma-2.html"], ["2010/02/02/good-quote-7/index.html", "/posts/2010/02/02/good-quote-7.html"], ["2004/10/27/linus-on-taking-up-and-working-on-open-source-projects/index.html", "/posts/2004/10/27/linus-on-taking-up-and-working-on-open-source-projects.html"], ["2007/12/31/books-i-could-read-this-year/index.html", "/posts/2007/12/31/books-i-could-read-this-year.html"], ["2014/06/23/meenakshi-amman-temple-in-minecraft-blueprints-and-plans/index.html", "/posts/2014/06/23/meenakshi-amman-temple-in-minecraft-blueprints-and-plans.html"], ["2013/04/04/meeting-with-bram-cohen/index.html", "/posts/2013/04/04/meeting-with-bram-cohen.html"], ["2004/05/28/next-foldoc-entry-to-edit-josephson-junction/index.html", "/posts/2004/05/28/next-foldoc-entry-to-edit-josephson-junction.html"], ["2013/06/15/space-center-here-we-come-to-visit-you/index.html", "/posts/2013/06/15/space-center-here-we-come-to-visit-you.html"], ["2005/01/21/ode-to-a-school-computer/index.html", "/posts/2005/01/21/ode-to-a-school-computer.html"], ["2012/12/22/conquer/index.html", "/posts/2012/12/22/conquer.html"], ["2008/12/18/just-for-the-record/index.html", "/posts/2008/12/18/just-for-the-record.html"], ["2014/07/02/south-tower-under-moon/index.html", "/posts/2014/07/02/south-tower-under-moon.html"], ["2007/01/28/flower-show-at-lalbagh/index.html", "/posts/2007/01/28/flower-show-at-lalbagh.html"], ["2009/02/27/good-quote-4/index.html", "/posts/2009/02/27/good-quote-4.html"], ["2007/07/11/patch-howto/index.html", "/posts/2007/07/11/patch-howto.html"], ["2006/06/20/recent-books-and-movies/index.html", "/posts/2006/06/20/recent-books-and-movies.html"], ["2010/05/27/scientific-truth/index.html", "/posts/2010/05/27/scientific-truth.html"], ["2013/10/12/using-my-photo-for-endorsement-google-gone-crazy/index.html", "/posts/2013/10/12/using-my-photo-for-endorsement-google-gone-crazy.html"], ["2008/08/14/quote-of-the-day-5/index.html", "/posts/2008/08/14/quote-of-the-day-5.html"], ["2005/08/24/web-updates/index.html", "/posts/2005/08/24/web-updates.html"], ["2015/06/07/uttama-villian/index.html", "/posts/2015/06/07/uttama-villian.html"], ["2010/07/02/the-timeless-way/index.html", "/posts/2010/07/02/the-timeless-way.html"], ["2010/07/15/quote-of-the-day-6/index.html", "/posts/2010/07/15/quote-of-the-day-6.html"], ["2011/05/27/division-of-human-energies/index.html", "/posts/2011/05/27/division-of-human-energies.html"], ["2006/07/13/its-been-sometime/index.html", "/posts/2006/07/13/its-been-sometime.html"], ["2004/12/22/torvalds-again/index.html", "/posts/2004/12/22/torvalds-again.html"], ["2006/11/12/article-on-maths/index.html", "/posts/2006/11/12/article-on-maths.html"], ["2009/06/16/the-pasta-theory-of-design/index.html", "/posts/2009/06/16/the-pasta-theory-of-design.html"], ["2006/12/03/annoucement-pyljvim-0-0-3-released/index.html", "/posts/2006/12/03/annoucement-pyljvim-0-0-3-released.html"], ["2009/02/07/paid-300-as-bribe-to-a-policewala/index.html", "/posts/2009/02/07/paid-300-as-bribe-to-a-policewala.html"], ["2005/05/01/did-a-bungee/index.html", "/posts/2005/05/01/did-a-bungee.html"], ["2010/01/28/change-is-transparent-to-users/index.html", "/posts/2010/01/28/change-is-transparent-to-users.html"], ["2007/08/07/quote-for-the-day/index.html", "/posts/2007/08/07/quote-for-the-day.html"], ["2005/07/04/war-of-the-worlds/index.html", "/posts/2005/07/04/war-of-the-worlds.html"], ["2009/09/28/good-quote-6/index.html", "/posts/2009/09/28/good-quote-6.html"], ["2005/09/20/nice-quote/index.html", "/posts/2005/09/20/nice-quote.html"], ["2004/12/21/httputhcode-sarovar-org/index.html", "/posts/2004/12/21/httputhcode-sarovar-org.html"], ["2009/01/03/madhava-of-sangamagrama/index.html", "/posts/2009/01/03/madhava-of-sangamagrama.html"], ["2008/06/10/j-k-rowling-on-failure-imagination-and-life/index.html", "/posts/2008/06/10/j-k-rowling-on-failure-imagination-and-life.html"], ["2013/09/03/introduction-to-programming-problem-solving-using-java-at-udacity/index.html", "/posts/2013/09/03/introduction-to-programming-problem-solving-using-java-at-udacity.html"], ["2008/12/13/the-agony-and-the-ecstasy/index.html", "/posts/2008/12/13/the-agony-and-the-ecstasy.html"], ["2005/06/05/rapple/index.html", "/posts/2005/06/05/rapple.html"], ["2007/03/14/happy-pi-day-2/index.html", "/posts/2007/03/14/happy-pi-day-2.html"], ["2010/11/29/bruce-lee-quote/index.html", "/posts/2010/11/29/bruce-lee-quote.html"], ["2004/06/18/good-quote-9/index.html", "/posts/2004/06/18/good-quote-9.html"], ["2014/06/20/the-incredibles-bill-and-melida-gates-on-humanity/index.html", "/posts/2014/06/20/the-incredibles-bill-and-melida-gates-on-humanity.html"], ["2009/02/15/yahoo-hack-day-india-2009/index.html", "/posts/2009/02/15/yahoo-hack-day-india-2009.html"], ["2014/06/23/madurai-meenakshi-temple-in-minecraft-day-2/index.html", "/posts/2014/06/23/madurai-meenakshi-temple-in-minecraft-day-2.html"], ["2006/11/24/whatzup-lyf/index.html", "/posts/2006/11/24/whatzup-lyf.html"], ["2014/07/04/walls-of-the-temple-and-how-it-should-look-finally/index.html", "/posts/2014/07/04/walls-of-the-temple-and-how-it-should-look-finally.html"], ["2014/07/05/fenches-around-the-temple-towers/index.html", "/posts/2014/07/05/fenches-around-the-temple-towers.html"], ["2012/12/24/two-things-that-i-been-etched-in-my-mind-about-sachin/index.html", "/posts/2012/12/24/two-things-that-i-been-etched-in-my-mind-about-sachin.html"], ["2007/02/18/lunar-new-year/index.html", "/posts/2007/02/18/lunar-new-year.html"], ["2007/03/23/karate-2nd-year/index.html", "/posts/2007/03/23/karate-2nd-year.html"], ["2009/09/14/good-quote-5/index.html", "/posts/2009/09/14/good-quote-5.html"], ["2007/01/27/no-citations-from-wikipedia/index.html", "/posts/2007/01/27/no-citations-from-wikipedia.html"], ["2009/01/05/to-iterate-is-human-to-recur-divine-%e2%80%a6/index.html", "/posts/2009/01/05/to-iterate-is-human-to-recur-divine-a.html"], ["2007/11/14/lambda-functions/index.html", "/posts/2007/11/14/lambda-functions.html"], ["2014/06/23/madurai-meenakshi-temple-in-minecraft-next-step-north-tower/index.html", "/posts/2014/06/23/madurai-meenakshi-temple-in-minecraft-next-step-north-tower.html"], ["2014/06/23/madurai-meenakshi-temple-in-minecraft-idea-phase/index.html", "/posts/2014/06/23/madurai-meenakshi-temple-in-minecraft-idea-phase.html"], ["2011/05/06/a-simple-thought-on-programming/index.html", "/posts/2011/05/06/a-simple-thought-on-programming.html"], ["2014/06/30/three-towers-under-construction/index.html", "/posts/2014/06/30/three-towers-under-construction.html"], ["2007/04/12/soc-application-accepted/index.html", "/posts/2007/04/12/soc-application-accepted.html"], ["2009/04/12/good-quote-on-life/index.html", "/posts/2009/04/12/good-quote-on-life.html"], ["2006/12/28/xmas-tree-decoration-contest/index.html", "/posts/2006/12/28/xmas-tree-decoration-contest.html"], ["2006/11/10/mahatma-gandhis-letters-to-adolf-hitler/index.html", "/posts/2006/11/10/mahatma-gandhis-letters-to-adolf-hitler.html"], ["2004/12/24/rms-is-totally-black-and-white/index.html", "/posts/2004/12/24/rms-is-totally-black-and-white.html"], ["2015/06/14/mapping-programming-to-mathematics/index.html", "/posts/2015/06/14/mapping-programming-to-mathematics.html"], ["2007/02/27/karate-in-the-morning/index.html", "/posts/2007/02/27/karate-in-the-morning.html"], ["2004/08/11/re-foldoc-entry-to-edit-matt-new-definition/index.html", "/posts/2004/08/11/re-foldoc-entry-to-edit-matt-new-definition.html"], ["2008/07/16/paninis-grammer/index.html", "/posts/2008/07/16/paninis-grammer.html"], ["2013/03/10/book-review-the-startup-of-you/index.html", "/posts/2013/03/10/book-review-the-startup-of-you.html"], ["2012/10/25/a-plan-for-the-improvement-of-english-spelling/index.html", "/posts/2012/10/25/a-plan-for-the-improvement-of-english-spelling.html"], ["2014/06/19/maker-faire-2014/index.html", "/posts/2014/06/19/maker-faire-2014.html"], ["2008/12/28/greedy-vs-non-greedy-in-re-good-example/index.html", "/posts/2008/12/28/greedy-vs-non-greedy-in-re-good-example.html"]]

# Presets of commands to execute to deploy. Can be anything, for
# example, you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola plugin -i ping`).  Or run `nikola check -l`.
# You may also want to use github_deploy (see below).
# You can define multiple presets and specify them as arguments
# to `nikola deploy`.  If no arguments are specified, a preset
# named `default` will be executed.  You can use as many presets
# in a `nikola deploy` command as you like.


deploy_token = os.getenv('SENTHIL_LEARN_TO_SOLVE_IT_TOKEN')

deploy_command = "cd output && surfer put --token " + deploy_token + "  --server senthil.learntosolveit.com * /"

DEPLOY_COMMANDS = {
     'default': [ deploy_command ]
}

# For user.github.io OR organization.github.io pages, the DEPLOY branch
# MUST be 'master', and 'gh-pages' for other repositories.

GITHUB_SOURCE_BRANCH = 'master'
GITHUB_DEPLOY_BRANCH = 'gh-pages'

# The name of the remote where you wish to push to, using github_deploy.
GITHUB_REMOTE_NAME = 'origin'

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, only .php files uses filters to inject PHP into
# Nikola’s templates. All other filters must be enabled through FILTERS.
#
# Many filters are shipped with Nikola. A list is available in the manual:
# <https://getnikola.com/handbook.html#post-processing-filters>
#
# from nikola import filters
# FILTERS = {
#    ".html": [filters.typogrify],
#    ".js": [filters.closure_compiler],
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.atom', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# Compiler to process LESS files.
# LESS_COMPILER = 'lessc'

# A list of options to pass to the LESS compiler.
# Final command is: LESS_COMPILER LESS_OPTIONS file.less
# LESS_OPTIONS = []

# Compiler to process Sass files.
# SASS_COMPILER = 'sass'

# A list of options to pass to the Sass compiler.
# Final command is: SASS_COMPILER SASS_OPTIONS file.s(a|c)ss
# SASS_OPTIONS = []

# #############################################################################
# Image Gallery Options
# #############################################################################

# One or more folders containing galleries. The format is a dictionary of
# {"source": "relative_destination"}, where galleries are looked for in
# "source/" and the results will be located in
# "OUTPUT_PATH/relative_destination/gallery_name"
# Default is:
# GALLERY_FOLDERS = {"galleries": "galleries"}
# More gallery options:
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []
#
# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True
#
# Folders containing images to be used in normal posts or pages. Images will be
# scaled down according to IMAGE_THUMBNAIL_SIZE and MAX_IMAGE_SIZE options, but
# will have to be referenced manually to be visible on the site
# (the thumbnail has ``.thumbnail`` added before the file extension).
# The format is a dictionary of {source: relative destination}.

IMAGE_FOLDERS = {'images': 'images'}
# IMAGE_THUMBNAIL_SIZE = 400

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to ' old posts, page %d' or ' page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
#
# (translatable) If the following is empty, defaults to BLOG_TITLE:
# INDEXES_TITLE = ""
#
# (translatable) If the following is empty, defaults to ' [old posts,] page %d' (see above):
# INDEXES_PAGES = ""
#
# If the following is True, INDEXES_PAGES is also displayed on the main (the
# newest) index page (index.html):
# INDEXES_PAGES_MAIN = False
#
# If the following is True, index-1.html has the oldest posts, index-2.html the
# second-oldest posts, etc., and index.html has the newest posts. This ensures
# that all posts on index-x.html will forever stay on that page, now matter how
# many new posts are added.
# If False, index-1.html has the second-newest posts, index-2.html the third-newest,
# and index-n.html the oldest posts. When this is active, old posts can be moved
# to other index pages when new posts are added.
# INDEXES_STATIC = True
#
# (translatable) If PRETTY_URLS is set to True, this setting will be used to create
# prettier URLs for index pages, such as page/2/index.html instead of index-2.html.
# Valid values for this settings are:
#   * False,
#   * a list or tuple, specifying the path to be generated,
#   * a dictionary mapping languages to lists or tuples.
# Every list or tuple must consist of strings which are used to combine the path;
# for example:
#     ['page', '{number}', '{index_file}']
# The replacements
#     {number}     --> (logical) page number;
#     {old_number} --> the page number inserted into index-n.html before (zero for
#                      the main page);
#     {index_file} --> value of option INDEX_FILE
# are made.
# Note that in case INDEXES_PAGES_MAIN is set to True, a redirection will be created
# for the full URL with the page number of the main page to the normal (shorter) main
# page URL.
# INDEXES_PRETTY_PAGE_URL = False

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of:
# algol
# algol_nu
# arduino
# autumn
# borland
# bw
# colorful
# default
# emacs
# friendly
# fruity
# igor
# lovelace
# manni
# monokai
# murphy
# native
# paraiso_dark
# paraiso_light
# pastie
# perldoc
# rrt
# tango
# trac
# vim
# vs
# xcode
# This list MAY be incomplete since pygments adds styles every now and then.
# CODE_COLOR_SCHEME = 'default'

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONFIG_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONFIG_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# FAVICONS contains (name, file, size) tuples.
# Used to create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# FAVICONS = (
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# )

# Show teasers (instead of full posts) in indexes? Defaults to False.
# INDEX_TEASERS = False

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the feeds, if FEED_TEASERS is True (translatable)
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

# Append a URL query to the FEED_READ_MORE_LINK in Atom and RSS feeds. Advanced
# option used for traffic source tracking.
# Minimum example for use with Piwik: "pk_campaign=feed"
# The following tags exist and are replaced for you:
# {feedRelUri}                  A relative link to the feed.
# {feedFormat}                  The name of the syndication format.
# Example using replacement for use with Google Analytics:
# "utm_source={feedRelUri}&utm_medium=nikola_feed&utm_campaign={feedFormat}_feed"
FEED_LINKS_APPEND_QUERY = False

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = ""
# I recommend using the Creative Commons' wizard:
# https://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="https://getnikola.com" rel="nofollow">Nikola</a>         {license}'

# Things that will be passed to CONTENT_FOOTER.format().  This is done
# for translatability, as dicts are not formattable.  Nikola will
# intelligently format the setting properly.
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format().  For example, {'en': (('Hello'), {'target': 'World'})}
# results in CONTENT_FOOTER['en'].format('Hello', target='World').
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
# (translatable)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

COMMENT_SYSTEM = False

COMMENT_SYSTEM_ID = "xtoinfinity"

# Enable annotations using annotateit.org?
# If set to False, you can still enable them for individual posts and pages
# setting the "annotations" metadata.
# If set to True, you can disable them for individual posts and pages using
# the "noannotations" metadata.
# ANNOTATIONS = False

# Create index.html for page (story) folders?
# WARNING: if a page would conflict with the index file (usually
#          caused by setting slug to `index`), the STORY_INDEX
#          will not be generated for that directory.
# STORY_INDEX = False
# Enable comments on story pages?
# COMMENTS_IN_STORIES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
# INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
STRIP_INDEXES = False

# Should the sitemap list directories which only include other directories
# and no files.
# Default to True
# If this is False
# e.g. /2012 includes only /01, /02, /03, /04, ...: don't add it to the sitemap
# if /2012 includes any files (including index.html)... add it to the sitemap
# SITEMAP_INCLUDE_FILELESS_DIRS = True

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.

# ROBOTS_EXCLUSIONS = ["/"]

# Instead of putting files in <slug>.html, put them in <slug>/index.html.
# No web server configuration is required. Also enables STRIP_INDEXES.
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata.
PRETTY_URLS = False

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts by default
# SCHEDULE_ALL = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
# MATHJAX_CONFIG = """
# <script type="text/x-mathjax-config">
# MathJax.Hub.Config({
#     tex2jax: {
#         inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#         displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
#         processEscapes: true
#     },
#     displayAlign: 'left', // Change this to 'center' to center equations.
#     "HTML-CSS": {
#         styles: {'.MathJax_Display': {"margin": 0}}
#     }
# });
# </script>
# """

# Want to use KaTeX instead of MathJax? While KaTeX is less featureful,
# it's faster and the output looks better.
# If you set USE_KATEX to True, you also need to add an extra CSS file
# like this:
# EXTRA_HEAD_DATA = """<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/KaTeX/0.3.0/katex.min.css">"""
# USE_KATEX = False

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuration you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# The default is ['fenced_code', 'codehilite']
MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite', 'extra']

# Extra options to pass to the pandoc comand.
# by default, it's empty, is a list of strings, for example
# ['-F', 'pandoc-citeproc', '--bibliography=/Users/foo/references.bib']
# PANDOC_OPTIONS = []

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty (which is
# the default right now)
# (translatable)
# SOCIAL_BUTTONS_CODE = """
# <!-- Social buttons -->
# <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
# <a class="addthis_button_more">Share</a>
# <ul><li><a class="addthis_button_facebook"></a>
# <li><a class="addthis_button_google_plusone_share"></a>
# <li><a class="addthis_button_linkedin"></a>
# <li><a class="addthis_button_twitter"></a>
# </ul>
# </div>
# <script src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
# <!-- End of social buttons -->
# """

# Show link to source for the posts?
# Formerly known as HIDE_SOURCELINK (inverse)
# SHOW_SOURCELINK = True
# Copy the source files for your pages?
# Setting it to False implies SHOW_SOURCELINK = False
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# By default, Nikola generates RSS files for the website and for tags, and
# links to it.  Set this to False to disable everything RSS-related.
# GENERATE_RSS = True

# By default, Nikola does not generates Atom files for indexes and links to
# them. Generate Atom for tags by setting TAG_PAGES_ARE_INDEXES to True.
# Atom feeds are built based on INDEX_DISPLAY_POST_COUNT and not FEED_LENGTH
# Switch between plain-text summaries and full HTML content using the
# FEED_TEASER option. FEED_LINKS_APPEND_QUERY is also respected. Atom feeds
# are generated even for old indexes and have pagination link relations
# between each other. Old Atom feeds with no changes are marked as archived.
# GENERATE_ATOM = False

# Only inlclude teasers in Atom and RSS feeds. Disabling include the full
# content. Defaults to True.
# FEED_TEASERS = True

# Strip HTML from Atom annd RSS feed summaries and content. Defaults to False.
# FEED_PLAIN = False

# Number of posts in Atom and RSS feeds.
# FEED_LENGTH = 10

# Include preview image as a <figure><img></figure> at the top of the entry.
# Requires FEED_PLAIN = False. If the preview image is found in the content,
# it will not be included again. Image will be included as-is, aim to optmize
# the image source for Feedly, Apple News, Flipboard, and other popular clients.
# FEED_PREVIEWIMAGE = True

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a FeedBurner feed or something else.
# RSS_LINK = None

# A search form to search this site, for the sidebar. You can use a Google
# custom search (https://www.google.com/cse/)
# Or a DuckDuckGo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# (translatable)
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
# SEARCH_FORM = """
# <!-- DuckDuckGo custom search -->
# <form method="get" id="search" action="//duckduckgo.com/"
#  class="navbar-form pull-left">
# <input type="hidden" name="sites" value="%s">
# <input type="hidden" name="k8" value="#444444">
# <input type="hidden" name="k9" value="#D51920">
# <input type="hidden" name="kt" value="h">
# <input type="text" name="q" maxlength="255"
#  placeholder="Search&hellip;" class="span2" style="margin-top: 4px;">
# <input type="submit" value="DuckDuckGo Search" style="visibility: hidden;">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL
#
# If you prefer a Google search form, here's an example that should just work:
# SEARCH_FORM = """
# <!-- Google custom search -->
# <form method="get" action="https://www.google.com/search" class="navbar-form navbar-right" role="search">
# <div class="form-group">
# <input type="text" name="q" class="form-control" placeholder="Search">
# </div>
# <button type="submit" class="btn btn-primary">
# 	<span class="glyphicon glyphicon-search"></span>
# </button>
# <input type="hidden" name="sitesearch" value="%s">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL

# Use content distribution networks for jQuery, twitter-bootstrap css and js,
# and html5shiv (for older versions of Internet Explorer)
# If this is True, jQuery and html5shiv are served from the Google CDN and
# Bootstrap is served from BootstrapCDN (provided by MaxCDN)
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Check for USE_CDN compatibility.
# If you are using custom themes, have configured the CSS properly and are
# receiving warnings about incompatibility but believe they are incorrect, you
# can set this to False.
# USE_CDN_WARNING = True

# Extra things you want in the pages HEAD tag. This will be added right
# before </head>
# (translatable)
# EXTRA_HEAD_DATA = ""
# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# (translatable)
BODY_END = """
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-71599453-1', 'auto');
  ga('send', 'pageview');

</script>
"""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

# If you hate "Filenames with Capital Letters and Spaces.md", you should
# set this to true.
FILE_METADATA_UNSLUGIFY_TITLES = True

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Open Graph Protocol data for enhancing link sharing and
# discoverability of your site on Facebook, Google+, and other services.
# Open Graph is enabled by default.
# USE_OPEN_GRAPH = True

# Nikola supports Twitter Card summaries, but they are disabled by default.
# They make it possible for you to attach media to Tweets that link
# to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit https://cards-dev.twitter.com/validator
#
# Uncomment and modify to following lines to match your accounts.
# Images displayed come from the `previewimage` meta tag.
# You can specify the card type by using the `card` parameter in TWITTER_CARD.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards
#     # 'card': 'summary',          # Card type, you can also use 'summary_large_image',
#                                   # see https://dev.twitter.com/cards/types
#     # 'site': '@website',         # twitter nick for the website
#     # 'creator': '@username',     # Username for the content creator / author.
# }

# If webassets is installed, bundle JS and CSS into single files to make
# site loading faster in a HTTP/1.1 environment but is not recommended for
# HTTP/2.0 when caching is used. Defaults to True.
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# Enabling hyphenation has been shown to break math support in some cases,
# use with caution.
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
DEMOTE_HEADERS = 1

# If you don’t like slugified file names ([a-z0-9] and a literal dash),
# and would prefer to use all the characters your file system allows.
# USE WITH CARE!  This is also not guaranteed to be perfect, and may
# sometimes crash Nikola, your web server, or eat your cat.
# USE_SLUGIFY = True

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.

GLOBAL_CONTEXT = {'blog_sidebar': """\
<div class="sidebar-module sidebar-module-inset">
<p>
There are far, far better things ahead than any we leave behind. -- C.S.Lewis
</p>

<div class="sidebar-module">
  <h4>Links</h4>
  <ol class="list-unstyled">
    <li><a href="https://www.xtoinfinity.com/resume/Senthil_Kumaran.pdf">Curriculum Vitae</a></li>
    <li><a href="https://scholar.google.com/citations?user=wkveFyQAAAAJ">Google Scholar</a></li>
    <li><a href="https://twitter.com/phoe6">Twitter @phoe6</a></li>
    <li><a href="https://github.com/orsenthil/">Github @orsenthil</a></li>
  </ol>
  <h4>Projects</h4>
  <ol class="list-unstyled">
    <li><a href="http://www.learntosolveit.com/">Learn To Solve It</a></li>
  </ol>
</div>
"""}


# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []

USE_TAG_METADATA = True

