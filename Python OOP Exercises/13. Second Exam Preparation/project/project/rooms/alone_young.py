from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)


    # def calculate_expenses(self):
    #     total = 0
    #     for i in self.appliances:
    #         total += i.get_monthly_expense()
    #     self.expenses = total
    #     return self.expenses
#
# ay = AloneYoung("test", 120)
# ay.calculate_expenses(ay.appliances)
# print(ay.expenses)