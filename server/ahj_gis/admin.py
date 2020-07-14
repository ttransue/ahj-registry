from django.contrib.gis import admin
from .models import *


class PolygonAdmin(admin.OSMGeoAdmin):

    search_fields = ('NAMELSAD', 'STATEABBR')


# Register your models here.
admin.site.register(Polygon, PolygonAdmin)
admin.site.register(County, admin.OSMGeoAdmin)
admin.site.register(City, admin.OSMGeoAdmin)
