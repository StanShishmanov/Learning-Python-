from project.software.software import Software
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware

class Hardware:

    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if self.check_capacity(software) and self.check_memory(software):
            self.software_components.append(software)
        else:
            raise ValueError("Software cannot be installed")

    def uninstall(self, software: Software):
        for s in self.software_components:
            if s == software:
                self.software_components.remove(s)

    def check_capacity(self, software):
        current_capacity_usage = sum(s.capacity_consumption for s in self.software_components)
        needed_capacity = current_capacity_usage + software.capacity_consumption
        if self.capacity >= needed_capacity:
            return True
        return False

    def check_memory(self, software):
        current_memory_usage = sum(s.memory_consumption for s in self.software_components)
        needed_memory = current_memory_usage + software.memory_consumption
        if self.memory >= needed_memory:
            return True
        return False

    def __repr__(self):
        components = 'None'
        if self.software_components:
            components = ', '.join([s.name for s in self.software_components])
        total_express = 0
        total_light = 0
        for s in self.software_components:
            if isinstance(s, ExpressSoftware):
                total_express += 1

        for s in self.software_components:
            if isinstance(s, LightSoftware):
                total_light += 1
        text = f"Hardware Component - {self.name}\n" \
               f"Express Software Components: " \
               f"{total_express}\n" \
               f"Light Software Components: " \
               f"{total_light}\n" \
               f"Memory Usage: {sum(s.memory_consumption for s in self.software_components)} / {self.memory}\n" \
               f"Capacity Usage: {sum(s.capacity_consumption for s in self.software_components)} / {self.capacity}\n" \
               f"Type: {self.type}\n" \
               f"Software Components: {components}"  # TODO here newline might be broken
        return text