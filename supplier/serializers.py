from rest_framework import serializers
from supplier.models import AddFlightList

class AddSerializer(serializers.ModelSerializer):
   class Meta:
      model= AddFlightList
      fields= ['d_from', 'd_to', 'airline_name', 'flight_no', 'dept_date_from', 'dept_date_to', 'dept_terminal', 'dept_arival', 'dept_time', 'arr_time', 'class_type', 'bag_info', 'fare_rule', 'fare_code', 'trip_type', 'dept_city_name', 'arr_city_name', 'dept_airport_code', 'arr_airport_code', 'dept_airport_name', 'arr_airport_name', 'basic_fare' ]