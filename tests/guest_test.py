import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guests = [
            Guest("Donald Trump"),      # 0
            Guest("Vladimir Putin"),    # 1
            Guest("Kim Jong Un"),       # 2
            Guest("James Hetfield"),    # 3
            Guest("Clif Burton"),       # 4
            Guest("Brian Scott"),       # 5
            Guest("Angus Young")        # 6
        ]
    def test_room_name(self):
        # check that room name is created correctly
        self.assertEqual(self.guests[0].name, "Donald Trump")
        self.assertEqual(self.guests[1].name, "Vladimir Putin")
        self.assertEqual(self.guests[5].name, "Brian Scott")  