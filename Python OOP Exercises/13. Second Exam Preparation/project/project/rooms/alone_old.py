from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, 1)
        self.appliances = []
        self.room_cost = 10

    # def calculate_expenses(self, *args):
    #     return self.expenses
