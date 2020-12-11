from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:

    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.get_hardware_by_name(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(software) # TODO CHECK IF RAISE IS AUTOMATIC
        except ValueError:
            return "Software cannot be installed"
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.get_hardware_by_name(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)  # TODO CHECK IF RAISE IS AUTOMATIC
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.get_hardware_by_name(hardware_name)
        software = System.get_software_by_name(software_name)
        if not hardware or not software_name:
            return "Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory_used = sum(s.memory_consumption for s in System._software)
        total_memory = sum(h.memory for h in System._hardware)
        total_capacity_used = sum(s.capacity_consumption for s in System._software)
        total_capacity = sum(h.capacity for h in System._hardware)
        text = f"System Analysis\nHardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_memory_used} / {total_memory}\n" \
               f"Total Capacity Taken: {total_capacity_used} / {total_capacity}"
        return text

    @staticmethod
    def system_split():
        text = ""
        for h in System._hardware:
            new_str = repr(h)
            text += new_str
        return text

    @staticmethod
    def get_hardware_by_name(h_name):
        for h in System._hardware:
            if h.name == h_name:
                return h

    @staticmethod
    def get_software_by_name(s_name):
        for s in System._software:
            if s.name == s_name:
                return s


System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
print(System.register_express_software("HDD", "Test2", 100, 100))
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())

""""
HDD --> 50 / 350
SSD --> 800/ 300

"""