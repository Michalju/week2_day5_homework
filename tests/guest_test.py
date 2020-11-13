import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guests = {
            "DonaldTrump" : Guest("Donald Trump"),         # 0
            "VladimirPutin" : Guest("Vladimir Putin"),     # 1
            "KimJongUn" : Guest("Kim Jong Un"),           # 2
            "JamesHetfield" : Guest("James Hetfield"),     # 3
            "ClifBurton" : Guest("Clif Burton"),           # 4
            "BrianScott" : Guest("Brian Scott"),           # 5
            "AngusYoung" : Guest("Angus Young")            # 6
        }
    def test_room_name(self):
        # check that room name is created correctly
        self.assertEqual(self.guests["DonaldTrump"].name, "Donald Trump")
        self.assertEqual(self.guests["VladimirPutin"].name, "Vladimir Putin")
        self.assertEqual(self.guests["BrianScott"].name, "Brian Scott")  