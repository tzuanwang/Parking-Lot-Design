"""
1. Vehicle Class
    - Child Classes: car(1), limo(2), truck(3)
2. Driver Class
    - own a vehicle
    - total payment
3. ParkingLot Class
    - Have multiple ParkingFloors
    - Vehicles will automatically be assigned the next available parking spot on the lowest floor
4. ParkingFloor Class
    - Have multiple parking spaces which have a size of 1 (no fractional spots)
5. ParkingSystem Class
    - vehicles can be parked for a variable number of hours
    - Drivers are charged after they remove their vehicle based on an hourly rate
    - If there is no capacity, the system should not assign a spot and should notify the driver
"""
from ParkingLot import ParkingLot
from ParkingSystem import ParkingSystem
from Driver import Driver
from Car import Car
from Truck import Truck
from Limo import Limo


parkingLot = ParkingLot(3, 2)
parkingSystem = ParkingSystem(parkingLot, 5)

driver1 = Driver(1, Car())
driver2 = Driver(2, Limo())
driver3 = Driver(3, Truck())

print(parkingSystem.park_vehicle(driver1))      # true
print(parkingSystem.park_vehicle(driver2))      # true
print(parkingSystem.park_vehicle(driver3))      # false

print(parkingSystem.remove_vehicle(driver1))    # true
print(parkingSystem.remove_vehicle(driver2))    # true
print(parkingSystem.remove_vehicle(driver3))    # false
