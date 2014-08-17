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
    osm_place_id = models.CharField(max_length=20, blank=True)
    formatted_address = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.formatted_address


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    lookup_address = models.CharField(max_length=100, blank=True)

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

    address = models.OneToOneField(Address, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.lookup_address:
            try:
                address = Address.objects.get(id=self.address.id)
            except AttributeError:
                address = Address()

            quoted_address = urllib.quote_plus(self.lookup_address.encode('UTF-8'))
            url = 'http://nominatim.openstreetmap.org/search?format=json' + \
                  '&addressdetails=1&countrycodes=de&accept-language=de' + \
                  '&limit=1&q='+quoted_address
            data = json.load(urllib2.urlopen(url))
            time.sleep(.5)
            if data:
                address.house_number = data[0]['address'].get('house_number', '')
                address.road = data[0]['address'].get('road', '')
                address.suburb = data[0]['address'].get('suburb', '')
                address.city = data[0]['address'].get('city', '')
                address.state = data[0]['address'].get('state', '')
                address.postcode = data[0]['address'].get('postcode', '')
                address.country = data[0]['address'].get('country', '')
                address.lat = data[0].get('lat', '')
                address.lon = data[0].get('lon', '')
                address.osm_place_id = data[0].get('place_id', '')
                address.formatted_address = address.road + ' ' + address.house_number + \
                    ', '+address.postcode + ' ' + address.city
                address.save()
            self.address = address
        super(Restaurant, self).save(*args, **kwargs)

    def get_lat_lon(self, reversed=False):
        if not self.address:
            return "(None)"
        elif reversed:
            return self.address.lon+','+self.address.lat
        else:
            return self.address.lat+','+self.address.lon
    get_lat_lon.short_description = 'Latitude, Longitude'

    def __unicode__(self):
        return self.name + ' ('+self.offerings+')'


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
        return self.url + ' ('+self.kind+')'
