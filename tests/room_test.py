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

    
    def test_room_check_in(self):
        # verify the check in function works
        self.rooms["Shite"].check_in(Guest("Donald Trump"))
        self.rooms["Shite"].check_in(Guest("Vladimir Putin"))
        self.rooms["Rock&Roll"].check_in(Guest("Angus Young"))
        self.rooms["Metal"].check_in(Guest("James Hetfield"))

        self.assertEqual(self.rooms["Shite"]._guests[0].name, "Donald Trump")
        self.assertEqual(self.rooms["Shite"]._guests[1].name, "Vladimir Putin")
        self.assertEqual(self.rooms["Rock&Roll"]._guests[0].name, "Angus Young")
        self.assertEqual(self.rooms["Metal"]._guests[0].name, "James Hetfield")    