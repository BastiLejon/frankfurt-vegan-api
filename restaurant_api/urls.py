from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from restaurant_api import views

urlpatterns = patterns('',
    # url(r'^$', 'api_root'),
    url(r'^restaurants/$', views.RestaurantList.as_view(), name='restaurant-list'),
    url(r'^restaurants/(?P<pk>[0-9]+)/$', views.RestaurantDetail.as_view(), name='restaurant-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
