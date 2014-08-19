from django.contrib import admin
from restaurant_api.models import Restaurant, Address, Website

from django import forms
from django.contrib.auth import models


class AddressAdmin(admin.ModelAdmin):
    """
    Adjust Address handling in Django admin
    """
    list_display = ('formatted_address', 'city', 'district', 'lat', 'lng',)
    list_filter = ['district', 'city', 'state', 'country']
    search_fields = ['formatted_address']


class WebsiteInline(admin.TabularInline):
    """
    Display Websites inline within Restaurants in Django admin
    """
    model = Website
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    """
    Adjust Restaurant handling in Django admin
    """
    fieldsets = [
        ('General information', {'fields': ['name', 'address', 'phone_number', ]}),
        ('Detailed information', {'fields': ['offerings', 'restaurant_type', ]}),
        (None, {'fields': ['comment']}),
        ('Other', {'fields': ['lookup_address'], 'classes': ['collapse']}),
    ]
    inlines = [WebsiteInline]
    list_display = ('name', 'address', 'offerings',
                    'get_lat_lng',)
    list_filter = ['offerings', 'last_modified', 'created']
    search_fields = ['name']


class WebsiteAdmin(admin.ModelAdmin):
    """
    Adjust Website handling in Django admin
    """
    list_display = ('url', 'kind',)
    list_filter = ['kind']
    search_fields = ['url']

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Website, WebsiteAdmin)
