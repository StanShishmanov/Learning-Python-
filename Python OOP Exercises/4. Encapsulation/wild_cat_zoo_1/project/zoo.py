# from project.caretaker import Caretaker
# from project.cheetah import Cheetah
# from project.keeper import Keeper
# from project.lion import Lion
# from project.tiger import Tiger
# from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, value):
        self.__animal_capacity = value

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, value):
            self.__workers_capacity = value

    def add_animal(self, animal, price):
        if price <= self.budget and self.animal_capacity > 0:
            self.animal_capacity -= 1
            self.animals.append(animal)
            self.budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif price > self.budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.workers_capacity > 0:
            self.workers.append(worker)
            self.workers_capacity -= 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.workers_capacity += 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary
        if self.budget - total_salaries > 0:
            self.budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_cost = 0
        for animal in self.animals:
            total_cost += animal.get_needs()
        if self.budget - total_cost > 0:
            self.budget -= total_cost
            return f"You tended all the animals. They are happy. Budget left: {self.budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.budget += amount

    def animals_status(self):
        text1 = f"You have {len(self.animals)} animals\n"
        total_lions = 0
        total_tigers = 0
        total_cheetas = 0
        lion_text = ""
        tiger_text = ""
        cheetah_text = ""

        for an in self.animals:
            if an.__class__.__name__ == "Lion":
                if total_lions > 0:
                    lion_text += '\n' + an.__repr__()
                    total_lions += 1
                else:
                    lion_text += an.__repr__()
                    total_lions += 1

            elif an.__class__.__name__ == "Tiger":
                if total_tigers > 0:
                    tiger_text += '\n' + an.__repr__()
                    total_tigers += 1
                else:
                    tiger_text += an.__repr__()
                    total_tigers += 1

            elif an.__class__.__name__ == "Cheetah":
                if total_cheetas > 0:
                    cheetah_text += '\n' + an.__repr__()
                    total_cheetas += 1
                else:
                    cheetah_text += an.__repr__()
                    total_cheetas += 1

        lion_length = f"----- {total_lions} Lions:\n"
        tiger_length = f"\n----- {total_tigers} Tigers:\n"
        cheetah_length = f"\n----- {total_cheetas} Cheetas:\n"

        return text1 + lion_length + lion_text + tiger_length + tiger_text + cheetah_length + cheetah_text

    def workers_status(self):
        text1 = f"You have {len(self.workers)} workers\n"
        total_keepers = 0
        total_caretakers = 0
        total_vets = 0
        keeper_text = ""
        caretaker_text = ""
        vet_text = ""
        for an in self.workers:
            if an.__class__.__name__ == "Keeper":
                if total_keepers > 0:
                    keeper_text += '\n' + an.__repr__()
                    total_keepers += 1
                else:
                    keeper_text += an.__repr__()
                    total_keepers += 1

            elif an.__class__.__name__ == "Caretaker":
                if total_caretakers > 0:
                    caretaker_text += '\n' + an.__repr__()
                    total_caretakers += 1
                else:
                    caretaker_text += an.__repr__()
                    total_caretakers += 1

            elif an.__class__.__name__ == "Vet":
                if total_vets > 0:
                    vet_text += '\n' + an.__repr__()
                    total_vets += 1
                else:
                    vet_text += an.__repr__()
                    total_vets += 1

        keeper_amount = f"----- {total_keepers} Keepers:\n"
        caretaker_amount = f"\n----- {total_caretakers} Caretakers:\n"
        vet_amount = f"\n----- {total_vets} Vets:\n"

        return text1 + keeper_amount + keeper_text + caretaker_amount + caretaker_text + vet_amount + vet_text
#
# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())