from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        self.calculate_expenses(self.appliances)

    # def calculate_expenses(self, *args):
    #     total = 0
    #     for i in self.appliances:
    #         total += i.get_monthly_expense()
    #     self.expenses = total
    #     return self.expenses
