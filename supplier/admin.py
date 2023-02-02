from django.contrib import admin
from supplier.models import AddFlightList

# Register your models here.

class AddPnr(admin.ModelAdmin):
   # list_display=['d_from', 'd_from', 'airline_name', 'flight_no', 'trip_type', 'basic_fare', 'dept_city_name', 'arr_city_name', 'arr_airport_name']
   pass
admin.site.register(AddFlightList, AddPnr)