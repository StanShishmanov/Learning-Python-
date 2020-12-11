from project.people.child import Child
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        # total = 0
        # for r in self.rooms:
        #     total += r.calculate_expenses() + r.room_cost
        # return f"Monthly consumption: {total:.2f}$."
        total = sum(r.cost for r in self.rooms)
        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        text = []
        for r in self.rooms:
            if r.budget >= r.cost:
                text.append(f"{r.family_name} paid {r.cost:.2f}$ and have {r.budget:.2f}$ left.")
                r.budget -= r.cost

            else:
                text.append(f"{r.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(r)
        return '\n'.join(text)

    def status(self):
        total_people = 0
        for r in self.rooms:
            total_people += r.members_count
        return '\n'.join(
            [
                f"Total population: {total_people}",
            ] + list(map(str, self.rooms))
        )
        # total_people = sum([p.members_count for p in self.rooms])
        # text = f"Total population: {total_people}\n"
        # for r in self.rooms:
        #     text += f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$\n"
        #     if r.children:
        #         for c in r.children:
        #             text += f"--- Child {r.children.index(c) + 1} monthly cost: {c.cost * 30:.2f}$\n"
        #     if r.appliances:
        #         ap_cost = sum([a.get_monthly_expense() for a in r.appliances])
        #         text += f"--- Appliances monthly cost: {ap_cost:.2f}$\n"

#
# everland = Everland()
# young_couple = YoungCouple("Johnsons", 150, 205)
#
# child_one = Child(5, 1, 2, 1)
# child_two = Child(3, 2)
# young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child_one, child_two)
#
# everland.add_room(young_couple)
# everland.add_room(young_couple_with_children)
#
# print(everland.get_monthly_consumptions())
# print(everland.pay())
# print(everland.status())
#
# everland = Everland()
# young_couple = YoungCouple("Johnsons", 150, 205)
#
# child1 = Child(5, 1, 2, 1)
# child2 = Child(3, 2)
# young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
# alone_old = AloneOld("Sam", 150)
#
# alone_young = AloneYoung("SamMlad", 1150)
# old_couple = OldCouple("Stari", 200, 250)
#
# everland.add_room(alone_old)
# everland.add_room(alone_young)
# everland.add_room(old_couple)
# everland.add_room(young_couple)
# everland.add_room(young_couple_with_children)
#
# print(everland.get_monthly_consumptions())
# print(everland.pay())
# print(everland.status())
