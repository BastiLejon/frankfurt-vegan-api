from django.conf.urls import patterns, url, include
from restaurant_api import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

"""from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from restaurant_api import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^restaurants/$', views.RestaurantList.as_view(), name='restaurant-list'),
    url(r'^restaurants/(?P<pk>[0-9]+)/$', views.RestaurantDetail.as_view(), name='restaurant-detail'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

urlpatterns = format_suffix_patterns(urlpatterns)
"""
