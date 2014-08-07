from rest_framework import serializers
from restaurant_api.models import Restaurant, Address, Website


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('formatted_address', 'lat', 'lon',)


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ('url', 'kind')


class RestaurantSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)
    websites = WebsiteSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'phone_number', 'websites',
                  'offerings', 'restaurant_type', 'comment',)
