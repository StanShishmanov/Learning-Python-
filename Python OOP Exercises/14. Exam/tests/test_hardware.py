import unittest
from project.hardware.hardware import Hardware
from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("test", "test_type", 10, 100)
        self.power_hardware = PowerHardware("power", 20, 50)
        self.heavy_hardware = HeavyHardware("heavy", 20, 50)
        self.light_software = LightSoftware("light", 10, 10)
        self.express_software = ExpressSoftware("express", 10, 10)

    def test_hardware(self):
        self.assertEqual('test', self.hardware.name)
        self.assertEqual("test_type", self.hardware.type)
        self.assertEqual(10, self.hardware.capacity)
        self.assertEqual(100, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_heavy_hardware(self):
        self.assertEqual('heavy', self.heavy_hardware.name)
        self.assertEqual("Heavy", self.heavy_hardware.type)
        self.assertEqual(40, self.heavy_hardware.capacity)
        self.assertEqual(37, self.heavy_hardware.memory)
        self.assertEqual([], self.heavy_hardware.software_components)

    def test_power_hardware(self):
        self.assertEqual('power', self.power_hardware.name)
        self.assertEqual("Power", self.power_hardware.type)
        self.assertEqual(5, self.power_hardware.capacity)
        self.assertEqual(87, self.power_hardware.memory)
        self.assertEqual([], self.power_hardware.software_components)

    def test_light_software(self):
        self.assertEqual('light', self.light_software.name)
        self.assertEqual("Light", self.light_software.type)
        self.assertEqual(15, self.light_software.capacity_consumption)
        self.assertEqual(5, self.light_software.memory_consumption)

    def test_express_software(self):
        self.assertEqual('express', self.express_software.name)
        self.assertEqual("Express", self.express_software.type)
        self.assertEqual(10, self.express_software.capacity_consumption)
        self.assertEqual(20, self.express_software.memory_consumption)

    def test_install_with_extra_capacity_or_memory_should_raise_value_error(self):
        light_software = LightSoftware("light", 1000, 1000)
        with self.assertRaises(ValueError) as ex:
            self.hardware.install(light_software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_install_check_installed_components(self):
        light_software = LightSoftware("light", 1, 10)
        self.assertEqual(len(self.hardware.software_components), 0)
        self.hardware.install(light_software)
        self.assertEqual(len(self.hardware.software_components), 1)

    def test_uninstall(self):
        light_software = LightSoftware("light", 1, 10)
        self.assertEqual(len(self.hardware.software_components), 0)
        self.hardware.install(light_software)
        self.assertEqual(len(self.hardware.software_components), 1)
        self.hardware.uninstall(light_software)
        self.assertEqual(len(self.hardware.software_components), 0)

    def test_light_components_length(self):
        count = 0
        ls = LightSoftware("light1", 1, 10)
        ls2 = LightSoftware("light2", 2, 20)
        self.hardware.install(ls)
        self.hardware.install(ls2)
        for s in self.hardware.software_components:
            if s.type == "Light":
                count += 1
        self.assertEqual(count, len(self.hardware.software_components))

    def test_express_components_length(self):
        count = 0
        ex = ExpressSoftware("express1", 1, 10)
        ex2 = ExpressSoftware("express2", 2, 20)
        self.hardware.install(ex)
        self.hardware.install(ex2)
        for s in self.hardware.software_components:
            if s.type == "Express":
                count += 1
        self.assertEqual(count, len(self.hardware.software_components))

    def test_custom_repr(self):
        ls = LightSoftware("light1", 1, 10)
        ex = ExpressSoftware("express1", 1, 10)
        self.hardware.install(ls)
        self.hardware.install(ex)
        self.assertEqual(
            repr(self.hardware),
            "Hardware Component - test\n"
            "Express Software Components: 1\n"
            "Light Software Components: 1\n"
            "Memory Usage: 25 / 100\n"
            "Capacity Usage: 2 / 10\n"
            "Type: test_type\n"
            "Software Components: light1, express1"
                         )


if __name__ == "__main__":
    unittest.main()


# class Hardware:
#     def __init__(self, name, type, capacity, memory):
#         self.name = name
#         self.type = type
#         self.capacity = capacity
#         self.memory = memory
#         self.software_components = []
#
#     def install(self, software):
#         if self.can_install(software):
#             self.software_components.append(software)
#         else:
#             raise Exception("Software cannot be installed")
#
#     def uninstall(self, software):
#         self.software_components.remove(software)
#
#     def get_light_software_components_count(self):
#         return len([s for s in self.software_components if s.type == "Light"])
#
#     def get_express_software_components_count(self):
#         return len([s for s in self.software_components if s.type == "Express"])
#
#     def can_install(self, software):
#         has_space = sum([s.capacity_consumption for s in self.software_components]) + software.capacity_consumption <= self.capacity
#         has_memory = sum([s.memory_consumption for s in self.software_components]) + software.memory_consumption <= self.memory
#         return has_memory and has_space
#
#     def __repr__(self):
#         result = [f"Hardware Component - {self.name}",
#                   f"Express Software Components: {self.get_express_software_components_count()}",
#                   f"Light Software Components: {self.get_light_software_components_count()}",
#                   f"Memory Usage: {sum([s.memory_consumption for s in self.software_components])} / {self.memory}",
#                   f"Capacity Usage: {sum([s.capacity_consumption for s in self.software_components])} / {self.capacity}",
#                   f"Type: {self.type}",
#                   f"Software Components: {', '.join([str(s) for s in self.software_components]) if self.software_components else 'None'}"]
#
#         return "\n".join(result)
#
# class Software:
#     def __init__(self, name:str, type:str, capacity_consumption:int, memory_consumption:int):
#         self.name = name
#         self.type = type
#         self.capacity_consumption = capacity_consumption
#         self.memory_consumption = memory_consumption
#
#     def __repr__(self):
#         return self.name
#
# from project.software.software import Software
#
#
# class ExpressSoftware(Software):
#     def __init__(self, name, capacity_consumption, memory_consumption):
#         super().__init__(name, "Express", int(capacity_consumption), int(memory_consumption * 2))
#
# from project.hardware.hardware import Hardware
# from project.software.express_software import ExpressSoftware
#
# class Test:
#     pass
