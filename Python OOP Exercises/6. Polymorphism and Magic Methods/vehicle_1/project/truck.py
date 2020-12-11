from project.vehicle import Vehicle


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, km):
        total_consumption = self.fuel_consumption + 1.6
        if not self.fuel_quantity < total_consumption * km:
            self.fuel_quantity -= total_consumption * km

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95

#
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
