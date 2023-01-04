#import classes ; importing classes.py, the whole file is executed when this file is runned 
#pytest is a library for using test framework, can be found from pypi.org or pip install pytest
import time
import pytest
from classes import Motorcycle, Car  #importing just only motorcycle and Car

print(Motorcycle) # accessing the motorcycle class from the classes.py

moto = Motorcycle('Triumph', 'Thruxton')
MyCar = Car('Toyota','Corolla')

for vehicles in [moto, MyCar]: #testing if the methods work as intended
    print(f'The time is {time.time()}')
    print(vehicles)
    vehicles.turn_engine_on()
    vehicles.turn_headlight_on()
    vehicles.start_driving()
    vehicles.turn('left')
    vehicles.turn('right')
    vehicles.stop_driving()
    vehicles.turn_engine_off()
    vehicles.turn_headlight_off()
    print(vehicles)
    print(type(vehicles))
    print()
    time.sleep(1) #Go to sleep for 1 second
    