from django.contrib import admin
from restaurant_api.models import Restaurant, Address, Website

from django import forms
from django.contrib.auth import models


class AddressAdmin(admin.ModelAdmin):
    list_display = ('formatted_address',)


class WebsiteInline(admin.TabularInline):
    model = Website
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': ['name', 'lookup_address', 'phone_number', ]}),
        ('Detailed information', {'fields': ['offerings', 'restaurant_type', ]}),
        (None, {'fields': ['comment']}),
        ('Other', {'fields': ['address'], 'classes': ['collapse']}),
    ]
    inlines = [WebsiteInline]
    list_display = ('name', 'address', 'get_lat_lng',
                    'offerings', 'last_modified',)

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Website)
