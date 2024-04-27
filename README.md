# Parking-Lot-Design

## Background
Parking lots have open spaces for vehicles to park in. Vehicles can be of different sizes, e.g. cars, limos, trucks, etc.

In some cases, parking spots can be numbered. For large venues, parking lots may have multiple levels, i.e. parking garages.

Sometimes parking is free, but in other cases customers have to pay. So parking lots can have a payment system to keep track of parked vehicles.

## Requirements
### Some possible questions to ask:
* Will there be multiple levels in the parking lot?
* What kinds of vehicles will be parked? Will their sizes differ?
* Will there be special spots for certain vehicles?
* Will the parking lot have a payment system? If so, how will it work?
* Will parking spots be reserved or can the driver choose any spot?
* How much functionality will the driver have beyond parking and paying?

## Basics
* Multiple levels in the parking lot
* Possible vehicle types: car, limo, semi-truck
* We will have a payment system, with a single entrance and exit
* Drivers will be assigned a parking spot after paying

## Vehicles and Parking Spots
* Vehicles can be of different sizes (car = 1, limo = 2, truck = 3)
* Each parking spot will have a size of 1
    - A vehicle must fully take up each spot assigned to it (no fractional spots)
* Vehicles will automatically be assigned the next available parking spot on the lowest floor

## Payment System
* Drivers will pay for parking and be assigned the next available spot on the lowest floor
* Drivers can pay for a variable number of hours and they are charged after they remove their vehicle based on an hourly rate
    - We can assume vehicles can be parked for a variable number of hours
* If there is no capacity, the system should not assign a spot and should notify the driver
