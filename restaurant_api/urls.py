from django.conf.urls import patterns, url, include
from restaurant_api import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)

# The API URLs are determined automatically by the router.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
