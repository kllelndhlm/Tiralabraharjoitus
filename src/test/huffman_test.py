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



##testaa järjestääkö ohjelma oikein
##esiintymistiheyden perusteella
##pienemmästä suurempaan
#    def test_jarjestaminen(self):
#        jarjestaminen = str(self.huffman.jarjestaminen())
#        self.assertEqual(jarjestaminen,
#        "[('T', 1), ('m', 1), ('o', 1), ('n', 1), ('k', 1), ('?', 1), ('!', 1), ('€', 1), ('ä', 2), (' ', 2), ('e', 2), ('s', 2), ('i', 2), ('t', 4)]")
#
#avaa testissä käytettävän tekstitiedoston
class TestHuffmanpurku(unittest.TestCase):
    def setUp(self):
        tiedostokysely = "../Tiralabraharjoitus/testiteksti.txt"
        with open(f"{tiedostokysely}", encoding="utf-8") as teksti:
            self.huffman_purku = Huffmanpurku("b'2   0001Y1T01R1E001W1\n1Q   >\xc6\x88'", "../Tiralabraharjoitus/testiteksti_huffman.bin")
