from battery import Nubbin_battery
from engine import willoughby_engine

class Rorschbach(Nubbin_battery, willoughby_engine):
    def __init__(self) -> None:
        super().__init__()
        self.engine = willoughby_engine
        self.battery = Nubbin_battery
    def needsService(self):
        return self.battery == True or self.engine == True