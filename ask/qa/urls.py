from django.conf.urls import patterns, include, url
#from ask.qa.views import *

#
# /
# /login/
# /signup/
# /question/<123>/
# /ask/
# /popular/
# /new/

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'views.main_page', name='main_page'),
    url(r'^login/', 'views.test', name='test'),
    url(r'^signup/', 'views.test', name='test'),
    url(r'^question/(?P<id>\d+)/', 'views.question', name='question'),
    url(r'^ask/', 'views.test', name='test'),
    url(r'^popular/', 'views.popular', name='popular'),
    url(r'^new/', 'views.test', name='test'),
)
