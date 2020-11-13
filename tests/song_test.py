import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.songs = {
            "NBT_Particles": Song("Nothing But Thieves", "Particles"),
            "NBT_Amsterdam": Song("Nothing But Thieves", "Amsterdam"),
            "ACDC_HighwayToHell": Song("AC/DC", "Highway To Hell"),
            "ACDC_TNT": Song("AC/DC", "TNT"),
            "ACDC_HellsBells": Song("AC/DC", "Hells Bells"),
            "ACDC_GirlsGotRhythm": Song("AC/DC", "Girls Got Rhythm"),
            "Metallica_SeekAndDestroy": Song("Metallica", "Seek And Destroy"),
            "Metallica_RideTheLighting": Song("Metallica", "Ride The Lighting"),
            "Metallica_Baterry": Song("Metallica", "Baterry"),
            "Slipknot_Unsainted": Song("Slipknot", "Unsainted")
        }

    def test_room_name(self):
        # check that song is created correctly
        self.assertEqual(self.songs["NBT_Particles"].artist, "Nothing But Thieves")
        self.assertEqual(self.songs["NBT_Particles"].title, "Particles")       
        self.assertEqual(self.songs["Metallica_RideTheLighting"].artist, "Metallica")
        self.assertEqual(self.songs["Metallica_RideTheLighting"].title, "Ride The Lighting")