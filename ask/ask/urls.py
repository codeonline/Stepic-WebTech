from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'', include('ask.qa.urls')),
]

