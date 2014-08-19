from django.db import models
import urllib
import urllib2
import json
import time


class Address(models.Model):
    """
    Address model, including relevant data received through
    Googles Geo API
    """
    house_number = models.CharField(max_length=20, blank=True)
    road = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    lat = models.CharField(max_length=30, blank=True)
    lng = models.CharField(max_length=30, blank=True)
    formatted_address = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.formatted_address


class Restaurant(models.Model):
    """
    Restaurant model, including fields used to describe vegan
    locations. lookup_address is used as a fuzzy field to
    receive to correct data through the Google Geo API.
    """
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
    TYPE_STORE = 'store'
    TYPE_CHOICES = (
        (TYPE_FAST_CASUAL, 'Fast casual'),
        (TYPE_FAST_FOOD, 'Fast food'),
        (TYPE_CASUAL_DINING, 'Casual dining'),
        (TYPE_FINE_DINING, 'Fine dining'),
        (TYPE_STORE, 'Store'),
    )
    restaurant_type = models.CharField(max_length=25, choices=TYPE_CHOICES,
                                       default=TYPE_FAST_CASUAL,)

    address = models.OneToOneField(Address, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Overrides save method to add Address object through lookup_address
        """
        if self.lookup_address:
            try:
                address = Address.objects.get(id=self.address.id)
            except AttributeError:
                address = Address()
            time.sleep(2)
            quoted_address = urllib.quote_plus(self.lookup_address.encode("UTF-8"))
            url = 'http://maps.googleapis.com/maps/api/geocode/json' + \
                  '?address='+quoted_address
            jsondata = json.load(urllib2.urlopen(url))
            all_components = jsondata['results'][0]['address_components']
            address.house_number = ''.join([c.get('long_name', '') for c in all_components if 'street_number' in c['types']][:1])
            address.road = ''.join([c.get('long_name', '') for c in all_components if 'route' in c['types']][:1])
            address.district = ''.join([c.get('long_name', '') for c in all_components if 'sublocality_level_2' in c['types']][:1])
            address.city = ''.join([c.get('long_name', '') for c in all_components if 'locality' in c['types']][:1])
            address.state = ''.join([c.get('long_name', '') for c in all_components if 'administrative_area_level_1' in c['types']][:1])
            address.postcode = ''.join([c.get('long_name', '') for c in all_components if 'postal_code' in c['types']][:1])
            address.country = ''.join([c.get('long_name', '') for c in all_components if 'country' in c['types']][:1])
            address.lat = jsondata["results"][0]["geometry"]["location"].get('lat', '')
            address.lng = jsondata["results"][0]["geometry"]["location"].get('lng', '')
            address.formatted_address = jsondata["results"][0].get('formatted_address', '')
            address.save()
            self.address = address
        super(Restaurant, self).save(*args, **kwargs)

    def get_lat_lng(self, reversed=False):
        """
        Return Latitude and Longitude to display in Django admin
        """
        if not self.address:
            return "(None)"
        elif reversed:
            return self.address.lng+','+self.address.lat
        else:
            return self.address.lat+','+self.address.lng
    get_lat_lng.short_description = 'Latitude, Longitude'

    def __unicode__(self):
        return self.name + ' ('+self.offerings+')'


class Website(models.Model):
    """
    Website model, including url and url-kind
    """
    restaurant = models.ForeignKey(Restaurant, related_name='websites')
    url = models.URLField(max_length=200)

    URL_TYPE_WEB = 'website'
    URL_TYPE_FACEBOOK = 'facebook'
    URL_TYPE_MENU = 'menu'
    URL_TYPE_CHOICES = (
        (URL_TYPE_WEB, 'Website'),
        (URL_TYPE_FACEBOOK, 'Facebook'),
        (URL_TYPE_MENU, 'Menu')
    )
    kind = models.CharField(max_length=10, choices=URL_TYPE_CHOICES,
                            default=URL_TYPE_WEB,)

    def __unicode__(self):
        return self.url + ' ('+self.kind+')'
