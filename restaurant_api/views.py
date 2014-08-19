from rest_framework import viewsets
from restaurant_api.models import Restaurant
from restaurant_api.serializers import RestaurantSerializer
from rest_framework import permissions


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Restaurant objects.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
