from rest_framework import viewsets
from restaurant_api.models import Restaurant
from restaurant_api.serializers import RestaurantSerializer
from rest_framework import permissions


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

"""
from restaurant_api.models import Restaurant
from restaurant_api.serializers import RestaurantSerializer
from rest_framework import generics
from rest_framework import permissions


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        'restaurants': reverse('restaurant-list', request=request, format=format)
    })
"""
