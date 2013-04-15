from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api

from hwdefio.hwdef.views import Home
from hwdefio.hwdef.api import HardwareResource


admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(HardwareResource())


urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
