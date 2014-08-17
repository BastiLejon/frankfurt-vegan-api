from rest_framework import serializers
from restaurant_api.models import Restaurant, Address, Website


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('formatted_address', 'lat', 'lon',)
        read_only_fields = ('formatted_address', 'lat', 'lon',)


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ('url', 'kind')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer(many=False, required=False)
    websites = WebsiteSerializer(many=True, required=False)

    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'phone_number', 'websites',
                  'offerings', 'restaurant_type', 'comment',)
