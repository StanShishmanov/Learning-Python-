from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float,  *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        self.children = list(children)

        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]
        for _ in range(len(children)):
            self.appliances.extend([TV(), Fridge(), Laptop()])

        self.calculate_expenses(self.appliances, self.children)

    # def calculate_expenses(self, *args):
    #     total = 0
    #     for i in self.appliances:
    #         total += i.get_monthly_expense()
    #     for c in self.children:
    #         total += c.cost * 30
    #     self.expenses = total
    #     return self.expenses


# child1 = Child(5, 1, 2, 1)
# child2 = Child(3, 2)
#
# yo = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
# print(yo.calculate_expenses())