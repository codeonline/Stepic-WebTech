from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Добавьте в urls.py  маршрут для следующих URL
# /
# /login/
# /signup/
# /question/<123>/    # вместо <123> - произвольный ID
# /ask/
# /popular/
# /new/

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^/', 'ask.views.test', name='test'),
    url(r'^login/', 'ask.views.test', name='test'),
    url(r'^signup/', 'ask.views.test', name='test'),
    url(r'^question/\d+', 'ask.views.test', name='test'),
    url(r'^ask/', 'ask.views.test', name='test'),
    url(r'^popular/', 'ask.views.test', name='test'),
    url(r'^new/', 'ask.views.test', name='test')
)

