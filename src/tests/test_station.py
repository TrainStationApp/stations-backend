import unittest
import station

class TestDigiTrafficStation(unittest.TestCase):

    def setUp(self):
        self.digiTraffic = station.DigiTrafficStation()

    def test_get_stops(self):
        stops = self.digiTraffic.get_stops()
        self.assertTrue(stops, ['Herttoniemi(M)'])
