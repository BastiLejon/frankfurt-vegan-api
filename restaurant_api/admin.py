from django.contrib import admin
from restaurant_api.models import Restaurant, Address, Website
# from reverseadmin import ReverseModelAdmin


class AddressAdmin(admin.ModelAdmin):
    list_display = ('formatted_address', 'place_id',)


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'kind',)


class WebsiteInline(admin.TabularInline):
    model = Website
    extra = 2


class RestaurantAdmin(admin.ModelAdmin):
    inlines = [WebsiteInline]
    list_display = ('name', 'address', 'get_lat_lon',
                    'offerings', 'created', 'last_modified',)

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Website, WebsiteAdmin)
