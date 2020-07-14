
class Aircraft():
    def __init__(self, model, tail_number, airline):
        self.model = model
        self.tail_number = tail_number
        self.airline = airline

class Plane(Aircraft):
    def __init__(self, model, tail_number, airline, capacity, num_rows, num_seats):
        super().__init__(model, tail_number, airline)
        self.capacity = capacity
        self.num_rows = num_rows
        self.num_seats = num_seats



class Helicopter(Aircraft):
    def __init__(self, model, tail_number, airline, capacity, num_seats):
        super().__init__(model, tail_number, airline)
        self.capacity = capacity
        self.num_seats = num_seats

