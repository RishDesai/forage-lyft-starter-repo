from abc import ABC

from car import Car
from datetime import *

class SpindlerBattery(Car, ABC):
    def __init__(self,last_service_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.currentDate = datetime.today().date()

    def needsService(self):
        return self.currentDate.year >= self.last_service_date.year + 2