from django.conf.urls import patterns, include, url
from django.contrib import admin

from hwdefio.hwdef.views import Home
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
