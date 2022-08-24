import imp
from engine import sternman_engine

from battery import Spindler_battery

class Palindrome(sternman_engine, Spindler_battery):
    def __init__(self) -> None:
        super().__init__()
        self.engine = sternman_engine
        self.battery = Spindler_battery
    
    def needsService(self):
        return self.battery == True or self.engine == True