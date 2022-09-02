import unittest
from huffman import Huffman

#avaa testissä käytettävän tekstitiedoston
class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.huffman = Huffman("QQ\nWERTY", "../Tiralabraharjoitus/testiteksti.txt")

#testaa avaako ohjelma oikean tiedoston
    def test_tulostus_oikein(self):
        tulostus = f"{self.huffman}"
        self.assertEqual(tulostus, "QQ\nWERTY")

#testaa laskeeko ohjelma oikean esiintymistiheyden
    def test_laske_esiintymistiheys(self):
        laske_esiintymistiheys = f"{self.huffman.laske_esiintymistiheys()}"
        self.assertEqual(laske_esiintymistiheys,
"{'Q': 2, '\\n': 1, 'W': 1, 'E': 1, 'R': 1, 'T': 1, 'Y': 1}")

#testaa palauttaako pakkaus oikein
    def test_pakkaus(self):
        pakkaus = f"{self.huffman.pakkaus()}"
        self.assertEqual(pakkaus,
"../Tiralabraharjoitus/testiteksti_huffman.bin")
