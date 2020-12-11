from project.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, km):
        total_consumption = self.fuel_consumption + 0.9
        if not total_consumption * km > self.fuel_quantity:
            self.fuel_quantity -= total_consumption * km

    def refuel(self, fuel):
        self.fuel_quantity += fuel

#
# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
