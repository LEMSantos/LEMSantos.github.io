AUTHOR = 'Lucas Eliaquim'
SITENAME = 'LEMSantos'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'docs/'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True





# Theme Settings
THEME = 'themes/brutalist'

SITEIMAGE = 'site-cover.jpg'
SITEDESCRIPTION = 'A simple, accessible, content-first Pelican theme inspired by David Bryant Copeland\'s https://brutalist-web.design/'

FAVICON = 'pelly.png'
LOGO = 'avatar.png'
FIRST_NAME = 'LEMSantos'
FANCY_NAME = 'Lucas Eliaquim'
## google analytics (fake code commented out)
GOOGLE_ANALYTICS = 'G-SW1LL2DZZ5'
ATTRIBUTION = True
## Other links can be added following the same tuple pattern
MENUITEMS = [
    ('Currículo', '/pages/resume.html'),
    ('Portfólio', '/pages/portfolio.html'),
]
GITHUB = 'https://github.com/lemsantos'
LINKEDIN = 'https://www.linkedin.com/in/lucas-eliaquim/'
MAIL='mailto:lemsantos.dev@gmail.com'
## Disqus Sitename for comments on posts
## Commenting mine out for this theme site
# DISQUS_SITENAME = 'brutalistpelican'
DISPLAY_PAGES_ON_MENU = False
