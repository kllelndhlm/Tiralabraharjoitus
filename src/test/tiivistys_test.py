import unittest
from tiivistys import Tiivistys


class TestTiivistys(unittest.TestCase):
    def setUp(self):
        self.tiivistys = Tiivistys("sana")

    def test_tulostus_oikein(self):
        tulostus = str(self.tiivistys)

        self.assertEqual(tulostus, "sana")
