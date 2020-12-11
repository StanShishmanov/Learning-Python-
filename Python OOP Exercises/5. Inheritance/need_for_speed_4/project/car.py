from project.vehicle import Vehicle


class Car(Vehicle):

    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

#
# vehicle = Vehicle(50, 150)
# print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
# print(vehicle.fuel)
# print(vehicle.horse_power)
# print(vehicle.fuel_consumption)
# vehicle.drive(100)
# print(vehicle.fuel)
# car = Car(150, 150)
# car.drive(50)
# print(car.fuel)
# car.drive(50)
# print(car.fuel)
# print(car.__class__.__bases__[0].__name__)