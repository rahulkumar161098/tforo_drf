from django.db import models

# Create your models here.
class AddFlightList(models.Model):
   d_from= models.CharField(max_length=30)
   d_to= models.CharField(max_length=30)
   airline_name= models.CharField(max_length=30)
   flight_no= models.IntegerField()
   dept_date_from= models.DateField()
   dept_date_to= models.DateField()
   dept_terminal= models.IntegerField()
   dept_arival= models.IntegerField()
   dept_time= models.TimeField()
   arr_time= models.TimeField()
   class_type= models.CharField(max_length=30)
   bag_info= models.IntegerField()
   fare_rule= models.CharField(max_length=30)
   fare_code= models.IntegerField()
   trip_type= models.CharField(max_length=5)
   dept_city_name= models.CharField(max_length=30)
   arr_city_name= models.CharField(max_length=30)
   dept_airport_code= models.CharField(max_length=30)
   arr_airport_code= models.CharField(max_length=30)
   dept_airport_name= models.CharField(max_length=40)
   arr_airport_name= models.CharField(max_length=40)
   basic_fare= models.IntegerField()

   def __str__(self):
      return self.airline_name

   # class meta:
   #    order= ('airline_name')