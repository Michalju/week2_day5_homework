import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.rooms = {
            "Shite" : Room("Shite"),
            "Rock&Roll" : Room("Rock&Roll"),
            "Metal" : Room("Metal")}

    def test_room_name(self):
        # check that room name is created correctly
        self.assertEqual(self.rooms["Shite"].name, "Shite")
        self.assertEqual(self.rooms["Rock&Roll"].name, "Rock&Roll")
        self.assertEqual(self.rooms["Metal"].name, "Metal")  