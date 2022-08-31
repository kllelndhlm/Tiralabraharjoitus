import unittest
from huffman import Huffman
from huffman_purku import Huffmanpurku
from lzw import Lzw
from lzw_purku import Lzwpurku

#avaa testissä käytettävän tekstitiedoston
class TestHuffman(unittest.TestCase):
    def setUp(self):
        tiedostokysely = "../Tiralabraharjoitus/testiteksti.txt"
        with open(f"{tiedostokysely}", encoding="utf-8") as teksti:
            self.huffman = Huffman("QQWERTY", "../Tiralabraharjoitus/testiteksti.txt")

#testaa avaako ohjelma oikean tiedoston
    def test_tulostus_oikein(self):
        tulostus = str(self.huffman)
        self.assertEqual(tulostus, "QQWERTY")

#testaa laskeeko ohjelma oikean esiintymistiheyden
    def test_laske_esiintymistiheys(self):
        laske_esiintymistiheys = str(self.huffman.laske_esiintymistiheys())
        self.assertEqual(laske_esiintymistiheys,
"{'Q': 2, 'W': 1, 'E': 1, 'R': 1, 'T': 1, 'Y': 1}")

    def test_pakkaus(self):
        pakkaus = str(self.huffman.pakkaus())
        self.assertEqual(pakkaus,
"../Tiralabraharjoitus/testiteksti_huffman.bin")



##testaa järjestääkö ohjelma oikein
##esiintymistiheyden perusteella
##pienemmästä suurempaan
#    def test_jarjestaminen(self):
#        jarjestaminen = str(self.huffman.jarjestaminen())
#        self.assertEqual(jarjestaminen,
#        "[('T', 1), ('m', 1), ('o', 1), ('n', 1), ('k', 1), ('?', 1), ('!', 1), ('€', 1), ('ä', 2), (' ', 2), ('e', 2), ('s', 2), ('i', 2), ('t', 4)]")
#
