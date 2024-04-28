class Driver:
    def __init__(self, id, vehicle):
        self._id = id
        self._vehicle = vehicle
        self._payment = 0

    def get_id(self):
        return self._id
    
    def get_vehicle(self):
        return self._vehicle
    
    def charge(self, amount):
        self._payment += amount