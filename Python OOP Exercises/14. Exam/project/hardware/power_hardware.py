from project.hardware.hardware import Hardware


class PowerHardware(Hardware):

    def __init__(self, name: str, capacity: int, memory: int):
        Hardware.__init__(self, name, "Power", int(capacity * 0.25), int(memory + (memory * 0.75)))
