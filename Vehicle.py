class Vehicle:

    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size
    
class Car(Vehicle):

    def __init__(self):
        super().__init__(1)

class Limo(Vehicle):

    def __init__(self):
        super().__init__(2)

class Truck(Vehicle):

    def __init__(self):
        super().__init__(3)