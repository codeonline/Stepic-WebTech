from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
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
     url(r'^login/', 'login', name='login'),     
     url(r'^logout/', 'logout', name='logout'),     
     url(r'^signup/', 'signup', name='signup'),     
     url(r'^question/(?P<id>\d+)/', 'question', name='question'),
     url(r'^ask/', 'ask', name='ask'),
     url(r'^popular/', 'popular', name='popular'),
     url(r'^new/', 'test', name='test'),
     url(r'^answer/', 'answer', name='answer'),
)
