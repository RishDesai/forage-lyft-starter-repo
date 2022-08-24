from engine import capulet_engine
from battery import Nubbin_battery

class Thovex(capulet_engine, Nubbin_battery):
    def __init__(self) -> None:
        super().__init__()
        self.engine = capulet_engine
        self.battery = Nubbin_battery
    def needsService(self):
        return self.battery == True or self.engine == True
    