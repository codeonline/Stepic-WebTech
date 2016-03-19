from django.conf.urls import patterns, include, url
#from qa.views import *

#
# /
# /login/
# /signup/
# /question/<123>/
# /ask/
# /popular/
# /new/

urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main_page', name='main_page'),
     url(r'^login/', 'test', name='test'),
     url(r'^signup/', 'test', name='test'),
     url(r'^question/(?P<id>\d+)/', 'question', name='question'),
     url(r'^ask/', 'test', name='test'),
     url(r'^popular/', 'popular', name='popular'),
     url(r'^new/', 'test', name='test'),
)
