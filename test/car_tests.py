from re import U
import unittest

from datetime import *
from Model.Calliope import Calliope

from abc import ABC
from Model.glissade import Glissade
from Model.palindrome import Palindrome
from Model.rorschach import Rorschbach
from Model.thovex import Thovex
from battery import*
from battery import Spindler_battery
from battery import Nubbin_battery
from car import Car
from engine import *

from Model import *
from engine import capulet_engine
from engine import willoughby_engine
from engine import sternman_engine

class TestCarCalliope(unittest.TestCase):
    def batteryOld(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 5)
        currentMiles = 0
        lastServicedMiles = 0
        capulet_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertTrue(Calliope(capulet_engine,Spindler_battery).needsService())
    
    def batteryNew(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 0
        lastServicedMiles = 0
        capulet_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertFalse(Calliope(capulet_engine,Spindler_battery).needsService())
    
    def engineUsed(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 34000
        lastServicedMiles = 0
        capulet_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertTrue(Calliope(capulet_engine,Spindler_battery).needsService())
    
    def engineNew(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 17000
        lastServicedMiles = 0
        capulet_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertFalse(Calliope(capulet_engine,Spindler_battery).needsService())

class TestCarGlissade(unittest.TestCase):
    def batteryOld(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 5)
        currentMiles = 0
        lastServicedMiles = 0
        willoughby_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertTrue(Glissade(willoughby_engine,Spindler_battery).needsService())

    def batteryNew(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 0
        lastServicedMiles = 0
        willoughby_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertFalse(Glissade(willoughby_engine,Spindler_battery).needsService())
        
    def energyUsed(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 61000
        lastServicedMiles = 0
        willoughby_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertTrue(Glissade(willoughby_engine,Spindler_battery).needsService())

    def energyNew(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 30000
        lastServicedMiles = 0
        willoughby_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertFalse(Glissade(willoughby_engine,Spindler_battery).needsService())


class TestCarPalindrome(unittest.TestCase):
    def batteryOld(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 5)
        currentMiles = 0
        lastServicedMiles = 0
        sternman_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertTrue(Palindrome(sternman_engine,Spindler_battery).needsService())

    def batteryNew(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 0
        lastServicedMiles = 0
        sternman_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertFalse(Palindrome(sternman_engine,Spindler_battery).needsService())
        
    def batteryOld(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 31000
        lastServicedMiles = 0
        sternman_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertTrue(Palindrome(sternman_engine,Spindler_battery).needsService())

    def energyUsed(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 30000
        lastServicedMiles = 0
        willoughby_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertTrue(Palindrome(sternman_engine,Spindler_battery).needsService())
    
    def energyNew(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 10000
        lastServicedMiles = 0
        willoughby_engine(lastServiced,currentMiles,lastServicedMiles)
        Spindler_battery(Car,ABC)
        self.assertFalse(Palindrome(sternman_engine,Spindler_battery).needsService())

class TestCarRorschach(unittest.TestCase):
    def batteryOld(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 5)
        currentMiles = 0
        lastServicedMiles = 0
        willoughby_engine(lastServiced,currentMiles,lastServicedMiles)
        Nubbin_battery(Car, ABC)
        self.assertTrue(Rorschbach(willoughby_engine,Nubbin_battery).needsService())


    def batteryNew(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 0
        lastServicedMiles = 0
        willoughby_engine(lastServiced,currentMiles,lastServicedMiles)
        Nubbin_battery(Car, ABC)
        self.assertFalse(Rorschbach(willoughby_engine,Nubbin_battery).needsService())
    
    def engineUsed(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 30000
        lastServicedMiles = 0
        willoughby_engine(lastServiced,currentMiles,lastServicedMiles)
        Nubbin_battery(Car, ABC)
        self.assertTrue(Rorschbach(willoughby_engine,Nubbin_battery).needsService())
    

    def engineNew(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 10000
        lastServicedMiles = 0
        willoughby_engine(lastServiced,currentMiles,lastServicedMiles)
        Nubbin_battery(Car, ABC)
        self.assertFalse(Rorschbach(willoughby_engine,Nubbin_battery).needsService())

class TestCarThovex(unittest.TestCase):

    def batteryOld(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 5)
        currentMiles = 0
        lastServicedMiles = 0
        capulet_engine(lastServiced,currentMiles, lastServicedMiles)
        Nubbin_battery(Car,ABC)
        self.assertTrue(Thovex(capulet_engine,Nubbin_battery).needsService())

    def batteryNew(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 0
        lastServicedMiles = 0
        capulet_engine(lastServiced,currentMiles, lastServicedMiles)
        Nubbin_battery(Car,ABC)
        self.assertFalse(Thovex(capulet_engine,Nubbin_battery).needsService())

    def engineUsed(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 30000
        lastServicedMiles = 0
        capulet_engine(lastServiced,currentMiles, lastServicedMiles)
        Nubbin_battery(Car,ABC)
        self.assertTrue(Thovex(capulet_engine,Nubbin_battery).needsService())
    
    def engineNew(self):
        today = datetime.today().date()
        currentYear = today.year
        lastServiced =  today.replace(year=today.year - 1)
        currentMiles = 10000
        lastServicedMiles = 0
        capulet_engine(lastServiced,currentMiles, lastServicedMiles)
        Nubbin_battery(Car,ABC)
        self.assertFalse(Thovex(capulet_engine,Nubbin_battery).needsService())






    




if __name__ == '__main__':
    unittest.main()
