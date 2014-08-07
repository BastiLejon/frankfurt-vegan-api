from django.db import models
from django.contrib.auth.models import User
import urllib
import urllib2
import json
import time


class Address(models.Model):
    house_number = models.CharField(max_length=20, blank=True)
    road = models.CharField(max_length=100, blank=True)
    suburb = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    lat = models.CharField(max_length=30, blank=True)
    lon = models.CharField(max_length=30, blank=True)
    place_id = models.CharField(max_length=20, blank=True)
    formatted_address = models.CharField(max_length=200, blank=True)

    """
    road = models.CharField(max_length=100, blank=True)
    street_number = models.CharField(max_length=20, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    locality = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    lat = models.CharField(max_length=30, blank=True)
    lng = models.CharField(max_length=30, blank=True)
    formatted_address = models.CharField(max_length=200, blank=True)
    """

    def __unicode__(self):
        return self.formatted_address


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    lookup_address = models.CharField(max_length=100)
    address = models.OneToOneField(Address, blank=True, related_name='address')

    phone_number = models.CharField(max_length=20, blank=True)
    comment = models.TextField(blank=True)

    OFFERING_VEGAN = 'vegan'
    OFFERING_VEGAN_OPTIONS = 'options'
    OFFERING_NO_VEGAN_OPTIONS = 'not_vegan'
    OFFERING_CHOICES = (
        (OFFERING_VEGAN, 'Vegan offering'),
        (OFFERING_VEGAN_OPTIONS, 'Vegan options'),
        (OFFERING_NO_VEGAN_OPTIONS, 'No vegan options'),
    )
    offerings = models.CharField(max_length=25, choices=OFFERING_CHOICES,
                                 default=OFFERING_VEGAN_OPTIONS,)

    TYPE_FAST_CASUAL = 'fast_casual'
    TYPE_FAST_FOOD = 'fast_food'
    TYPE_CASUAL_DINING = 'casual_dining'
    TYPE_FINE_DINING = 'fine_dining'
    TYPE_CHOICES = (
        (TYPE_FAST_CASUAL, 'Fast casual'),
        (TYPE_FAST_FOOD, 'Fast food'),
        (TYPE_CASUAL_DINING, 'Casual dining'),
        (TYPE_FINE_DINING, 'Fine dining'),
    )
    restaurant_type = models.CharField(max_length=25, choices=TYPE_CHOICES,
                                       default=TYPE_FAST_CASUAL,)

    owner = models.ForeignKey(User, related_name='restaurants')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        try:
            address = Address.objects.get(id=self.address.id)
        except DoesNotExist:
            address = Address()

        quoted_address = urllib.quote_plus(self.lookup_address.encode('UTF-8'))
        url = 'http://nominatim.openstreetmap.org/search?format=json' + \
              '&addressdetails=1&countrycodes=de&accept-language=de' + \
              '&limit=1&q='+quoted_address
        data = json.load(urllib2.urlopen(url))
        address.house_number = data[0]['address']['house_number']
        address.road = data[0]['address']['road']  # .encode("UTF-8")
        address.suburb = data[0]['address']['suburb']
        address.city = data[0]['address']['city']
        address.state = data[0]['address']['state']
        address.postcode = data[0]['address']['postcode']
        address.country = data[0]['address']['country']
        address.lat = data[0]['lat']
        address.lon = data[0]['lon']
        address.place_id = data[0]['place_id']
        address.formatted_address = address.road+' '+address.house_number+', '+address.postcode+' '+address.city

        """
        quoted_address = urllib.quote_plus(self.lookup_address.encode("UTF-8"))
        url = 'http://maps.googleapis.com/maps/api/geocode/json' + \
              '?address='+quoted_address
        jsondata = json.load(urllib2.urlopen(url))
        all_cmp = jsondata['results'][0]['address_components']
        type_filter = {'street_number', 'route', 'locality',
                       'administrative_area_level_1', 'country', 'postal_code'}
        cmps = [i for i in all_cmp if any(tf in type_filter for tf in i['types'])]
        address.route = cmps[1]['long_name'].encode("UTF-8")
        address.street_number = cmps[0]['long_name'].encode("UTF-8")
        address.postal_code = cmps[5]['long_name'].encode("UTF-8")
        address.locality = cmps[2]['long_name'].encode("UTF-8")
        address.area = cmps[3]['long_name'].encode("UTF-8")
        address.country = cmps[4]['long_name'].encode("UTF-8")
        address.lat = jsondata["results"][0]["geometry"]["location"]["lat"]
        address.lng = jsondata["results"][0]["geometry"]["location"]["lng"]
        address.formatted_address = jsondata["results"][0]["formatted_address"]
        """

        address.save()

        self.address = address
        time.sleep(.5)
        super(Restaurant, self).save(*args, **kwargs)

    def get_lat_lon(self, reversed=False):
        if reversed:
            return self.address.lon+','+self.address.lat
        else:
            return self.address.lat+','+self.address.lon
    # get_lat_lon.admin_order_field = 'lat'

    def __unicode__(self):
        return self.name

    # image_url = models.URLField(max_length=200, blank=True,
    # default='https://dl.dropboxusercontent.com/u/9692604/restaurant.jpg')

"""
    def save(self, *args, **kwargs):
        address = Address()
        quoted_address = urllib.quote_plus(self.lookup_address.encode("UTF-8"))
        url = 'http://maps.googleapis.com/maps/api/geocode/json' + \
              '?address='+quoted_address
        jsondata = json.load(urllib2.urlopen(url))
        all_cmp = jsondata['results'][0]['address_cmps']
        type_filter = {'street_number', 'route', 'locality',
                       'administrative_area_level_1', 'country', 'postal_code'}
        cmps = [i for i in all_cmp if any(tf in type_filter for tf in i['types'])]
        address.route = cmps[1]['long_name'].encode("UTF-8")
        address.street_number = cmps[0]['long_name'].encode("UTF-8")
        address.postal_code = cmps[5]['long_name'].encode("UTF-8")
        address.locality = cmps[2]['long_name'].encode("UTF-8")
        address.area = cmps[3]['long_name'].encode("UTF-8")
        address.country = cmps[4]['long_name'].encode("UTF-8")
        address.lat = jsondata["results"][0]["geometry"]["location"]["lat"]
        address.lng = jsondata["results"][0]["geometry"]["location"]["lng"]
        address.formatted_address = jsondata["results"][0]["formatted_address"]
        addr.save()

        self.address = address
        sleep(.3)
        super(Restaurant, self).save(*args, **kwargs)
"""


class Website(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='websites')

    url = models.URLField(max_length=200)

    URL_TYPE_WEB = 'website'
    URL_TYPE_FACEBOOK = 'facebook'
    URL_TYPE_CHOICES = (
        (URL_TYPE_WEB, 'Website'),
        (URL_TYPE_FACEBOOK, 'Facebook'),
    )
    kind = models.CharField(max_length=10, choices=URL_TYPE_CHOICES,
                            default=URL_TYPE_WEB,)

    def __unicode__(self):
        return self.url
