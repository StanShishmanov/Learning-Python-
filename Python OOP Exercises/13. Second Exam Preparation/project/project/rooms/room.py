# from project.appliances.appliance import Appliance
# from project.appliances.fridge import Fridge
# from project.appliances.tv import TV


class Room:

    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self._expenses = 0
        self.appliances = []

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        # total = 0
        # for l in args:
        #     for i in l:
        #         if isinstance(i, Appliance):
        #             total += i.get_monthly_expense()
        #         else:
        #             total += i.cost * 30
        # self.expenses = total
        # return self.expenses
        self.expenses = sum(el.get_monthly_expense() for seq in args for el in seq)

    @property
    def cost(self):
        return self.expenses * 30 + self.room_cost

    def __repr__(self):
        return '\n'.join([
            f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$"
        ] + [
            f"--- Child {idx + 1} monthly cost: {child.get_monthly_expense():.2f}$"
            for idx, child in enumerate(self.children)
        ] + [
            f"--- Appliances monthly cost: {sum(app.get_monthly_expense() for app in self.appliances ):.2f}$"
        ])

#
# room = Room("test", 500, 4)
# tv = TV()
# fridge = Fridge()
# room.appliances.append(tv)
# room.appliances.append(fridge)
# res = room.calculate_expenses()
# print(res)