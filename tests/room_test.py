import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.rooms = {
            "Pop" : Room("Pop"),
            "Rock&Roll" : Room("Rock&Roll"),
            "Metal" : Room("Metal")}

    def test_room_name(self):
        # check that room name is created correctly
        self.assertEqual(self.rooms["Pop"].name, "Pop")
        self.assertEqual(self.rooms["Rock&Roll"].name, "Rock&Roll")
        self.assertEqual(self.rooms["Metal"].name, "Metal")

    
    def test_room_check_in(self):
        # verify the check in function works
        self.rooms["Pop"].check_in(Guest("Donald Trump"))
        self.rooms["Pop"].check_in(Guest("Vladimir Putin"))
        self.rooms["Rock&Roll"].check_in(Guest("Angus Young"))
        self.rooms["Metal"].check_in(Guest("James Hetfield"))

        self.assertEqual(self.rooms["Pop"]._guests[0].name, "Donald Trump")
        self.assertEqual(self.rooms["Pop"]._guests[1].name, "Vladimir Putin")
        self.assertEqual(self.rooms["Rock&Roll"]._guests[0].name, "Angus Young")
        self.assertEqual(self.rooms["Metal"]._guests[0].name, "James Hetfield")   

    def test_room_check_out(self):
        # setting up the room with guests
        self.rooms["Pop"].check_in(Guest("Donald Trump"))
        self.rooms["Pop"].check_in(Guest("Vladimir Putin"))
        self.rooms["Rock&Roll"].check_in(Guest("Angus Young"))
        self.rooms["Rock&Roll"].check_in(Guest("Brian Scott"))
        self.rooms["Metal"].check_in(Guest("James Hetfield"))
        self.rooms["Metal"].check_in(Guest("Clif Burton"))

        # checking out all from room Pop
        self.assertEqual(len(self.rooms["Pop"]._guests), 2)
        self.rooms["Pop"].check_out("")
        self.assertEqual(len(self.rooms["Pop"]._guests), 0)   

        # checking out Brian Scott from Rock & Roll
        self.assertEqual(len(self.rooms["Rock&Roll"]._guests), 2)
        self.rooms["Rock&Roll"].check_out("Angus Young")
        self.assertEqual(len(self.rooms["Rock&Roll"]._guests), 1)
        self.assertEqual(self.rooms["Rock&Roll"]._guests[0].name, "Brian Scott")        
        
        # checking out Clif Burton from Metal
        self.assertEqual(len(self.rooms["Metal"]._guests), 2)
        self.rooms["Metal"].check_out("Clif Burton")
        self.assertEqual(len(self.rooms["Metal"]._guests), 1)
        self.assertEqual(self.rooms["Metal"]._guests[0].name, "James Hetfield")

    def test_room_add_songs(self):
        # adding songs to a room
        self.assertEqual(len(self.rooms["Pop"]._songs), 0) 
        self.assertEqual(len(self.rooms["Rock&Roll"]._songs), 0) 
        self.assertEqual(len(self.rooms["Metal"]._songs), 0) 

        self.rooms["Pop"].add_song(Song("Nothing But Thieves", "Particles"))
        self.rooms["Pop"].add_song(Song("Nothing But Thieves", "Amsterdam"))

        self.rooms["Rock&Roll"].add_song(Song("AC/DC", "Highway To Hell"))

        self.rooms["Metal"].add_song(Song("Metallica", "Baterry"))
        self.rooms["Metal"].add_song(Song("Metallica", "Seek And Destroy"))
        self.rooms["Metal"].add_song(Song("Slipknot", "Unsainted"))

        self.assertEqual(len(self.rooms["Pop"]._songs), 2) 
        self.assertEqual(len(self.rooms["Rock&Roll"]._songs), 1) 
        self.assertEqual(len(self.rooms["Metal"]._songs), 3)             
