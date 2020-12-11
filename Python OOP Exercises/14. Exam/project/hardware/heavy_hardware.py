from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class HeavyHardware(Hardware):

    def __init__(self, name: str, capacity: int, memory: int):
        Hardware.__init__(self, name, "Heavy", capacity * 2, int(memory * 0.75))

