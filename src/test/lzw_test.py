import unittest
from lzw import Lzw

#avaa testissä käytettävän tekstitiedoston
class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.lzw = Lzw("QQ\nWERTY", "../Tiralabraharjoitus/testiteksti.txt")

#testaa palauttaako pakkaus oikein
    def test_pakkaus(self):
        pakkaus = f"{self.lzw.pakkaus()}"
        self.assertEqual(pakkaus,
"../Tiralabraharjoitus/testiteksti_LZW.bin")
