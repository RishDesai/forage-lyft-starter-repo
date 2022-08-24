from battery import *
from battery import Spindler_battery
from engine import *
from engine import capulet_engine

class Calliope(capulet_engine, Spindler_battery):
    def __init__(self) -> None:
        super().__init__()
        self.engine = capulet_engine
        self.battery = Spindler_battery
    def needsService(self):
        return self.battery == True or self.engine == True