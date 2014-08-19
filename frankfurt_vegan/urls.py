from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from restaurant_api import urls

urlpatterns = patterns('',
    # url(r'^api/v1/', include('restaurant_api.urls')),
    url(r'^api/', include('restaurant_api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
