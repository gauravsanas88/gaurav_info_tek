from calendar_1 import *
from data_stream_ingestion import DataStream
from fuel_station_design import FuelStation

calendar = Calendar()
print(calendar.book(5,10))
print(calendar.book(8,13))
print(calendar.book(10,15))

print('*****'*10)
fuel_station = FuelStation(diesel=2,petrol=2,electric=1)
print(fuel_station.fuel_vheicle('diesel'))
print(fuel_station.fuel_vheicle('petrol'))
print(fuel_station.fuel_vheicle('diesel'))
print(fuel_station.fuel_vheicle('electric'))
print(fuel_station.fuel_vheicle('diesel'))
print(fuel_station.open_fuel_slot('diesel'))
print(fuel_station.fuel_vheicle('diesel'))
print(fuel_station.open_fuel_slot('electric'))
print(fuel_station.open_fuel_slot('electric'))

print('*****'*10)
data_stream = DataStream()
print(data_stream.should_output_data_str(timestamp=0,data_string='hello'))
print(data_stream.should_output_data_str(timestamp=1,data_string='world'))
print(data_stream.should_output_data_str(timestamp=6,data_string='hello'))
print(data_stream.should_output_data_str(timestamp=7,data_string='hello'))
print(data_stream.should_output_data_str(timestamp=8,data_string='world'))