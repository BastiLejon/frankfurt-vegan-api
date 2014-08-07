from django.contrib import admin
from restaurant_api.models import Restaurant, Address, Website
# from reverseadmin import ReverseModelAdmin


class AddressAdmin(admin.ModelAdmin):
    list_display = ('formatted_address', 'osm_place_id',)


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'kind',)


class WebsiteInline(admin.TabularInline):
    model = Website
    extra = 2


class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': ['name', 'lookup_address', ]}),
        ('Detailed information', {'fields': ['offerings', 'restaurant_type', ]}),
        (None, {'fields': ['comment']}),
        ('Other', {'fields': ['address', 'owner'], 'classes': ['collapse']}),
    ]
    # exclude = ('owner',)
    inlines = [WebsiteInline]
    list_display = ('name', 'address', 'get_lat_lon',
                    'offerings', 'created', 'last_modified',)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user # no need to check for it.
        obj.save()

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Website, WebsiteAdmin)

"""
class BugAdmin( admin.ModelAdmin ):
    fields = ['name', 'slug', 'summary', 'categories', 'status', 'browser', 'frequency', 'really_bug']
    exclude = ('author','excerpt')
    prepopulated_fields = { 'slug' : ['name'] }
    form = BugForm

    def save_form(self, request, form, change):
        obj = super( BugAdmin, self).save_form(request, form, change)
        if not change:
            obj.author = request.user
        return obj
"""
