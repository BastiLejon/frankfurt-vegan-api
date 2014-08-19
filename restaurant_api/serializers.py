from rest_framework import serializers
from restaurant_api.models import Restaurant, Address, Website


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('formatted_address', 'road', 'house_number', 'district', 'city', 'state', 'postcode', 'lat', 'lng',)
        read_only_fields = ('formatted_address', 'lat', 'lng',)


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ('id', 'url', 'kind',)


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer(many=False, required=False)
    websites = WebsiteSerializer(many=True, required=False, allow_add_remove=True)

    class Meta:
        model = Restaurant
        fields = ('url', 'name', 'lookup_address', 'address', 'phone_number',
                  'websites', 'offerings', 'restaurant_type', 'comment',)
        write_only_fields = ('lookup_address',)
