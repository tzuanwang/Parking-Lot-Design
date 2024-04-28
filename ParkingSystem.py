import datetime
import math
class ParkingSystem:
    def __init__(self, parkingLot, hourlyRate):
        self._parkingLot = parkingLot
        self._hourlyRate = hourlyRate
        self._timeParked = {} # map driverId to time that they parked

    def park_vehicle(self, driver):
        currentHour = datetime.datetime.now().hour
        isParked = self._parkingLot.park_vehicle(driver.get_vehicle())
        if isParked:
            self._timeParked[driver.get_id()] = currentHour
        return isParked
    
    def remove_vehicle(self, driver):
        if driver.get_id() not in self._timeParked:
            return False
        currentHour = datetime.datetime.now().hour
        timeParked = math.ceil(currentHour - self._timeParked[driver.get_id()])
        driver.charge(timeParked * self._hourlyRate)

        del self._timeParked[driver.get_id()]
        return self._parkingLot.remove_vehicle(driver.get_vehicle())
