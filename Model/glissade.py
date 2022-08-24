from engine import willoughby_engine
from battery import Spindler_battery

class Glissade(willoughby_engine, Spindler_battery):
    def __init__(self) -> None:
        super().__init__()
        self.engine = willoughby_engine
        self.battery = Spindler_battery
    
    def needsService(self):
        return self.battery == True or self.engine == True