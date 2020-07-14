
class Aircraft():
    def __init__(self, model, tail_number, airline):
        self.model = model
        self.tail_number = tail_number
        self.airline = airline

class Plane(Aircraft):
    def __init__(self, model, tail_number, airline, capacity):
        super().__init__(model, tail_number, airline)
        self.capacity = capacity



#class Helicopter(Aircraft):

