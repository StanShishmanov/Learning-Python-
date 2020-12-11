from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, km):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, km):
        total_consumption = self.fuel_consumption + 0.9
        if not total_consumption * km > self.fuel_quantity:
            self.fuel_quantity -= total_consumption * km

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, km):
        total_consumption = self.fuel_consumption + 1.6
        if not self.fuel_quantity < total_consumption * km:
            self.fuel_quantity -= total_consumption * km

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
