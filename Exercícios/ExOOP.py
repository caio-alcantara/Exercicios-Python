class Vehicle:
    color = 'White'

    def __init__(self, name, max_speed, mileage, seating_capacity=50):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, seating_capacity=50):
        self.seating_capacity = seating_capacity
        super().__init__(name, max_speed, mileage)

    def bus_model(self):
        return f"{self.name}, max speed: {self.max_speed}, mileage: {self.mileage}," \
               f" seating capacity: {self.seating_capacity}, color: {self.color}"

    def fare(self):
        return (self.seating_capacity * 100) + (0.1 * (self.seating_capacity * 100))


class Car(Vehicle):
    def __init__(self, name, max_speed, mileage, seating_capacity=5):
        self.seating_capacity = seating_capacity
        super().__init__(name, max_speed, mileage)

    def car_model(self):
        return f"{self.name}, max speed: {self.max_speed}, mileage: {self.mileage}, color: {self.color}"

    def fare(self):
        total = super().fare()
        return total


bus = Bus("Volvo", 65, 15000)
print(bus.bus_model())
car = Car("Tesla", 145, 1000)
print(car.car_model())
print(bus.fare())
print(car.fare())
