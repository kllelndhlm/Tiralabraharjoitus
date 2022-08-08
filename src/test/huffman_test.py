import unittest
from huffman import Huffman

#avaa testissä käytettävän tekstitiedoston
class TestHuffman(unittest.TestCase):
    def setUp(self):
        with open("../Tiralabraharjoitus/src/test/testiteksti.md", encoding="utf-8") as teksti:
            self.huffman = Huffman(teksti.read())

#testaa avaako ohjelma oikean tiedoston
    def test_tulostus_oikein(self):
        tulostus = str(self.huffman)
        self.assertEqual(tulostus, "Tämä on testiteksti?!€")

#testaa laskeeko ohjelma oikean esiintymistiheyden
    def test_esiintymistiheys(self):
        esiintymistiheys = str(self.huffman.esiintymistiheys())
        self.assertEqual(esiintymistiheys,
        "{'T': 1, 'ä': 2, 'm': 1, ' ': 2, 'o': 1, 'n': 1, 't': 4, \
'e': 2, 's': 2, 'i': 2, 'k': 1, '?': 1, '!': 1, '€': 1}")

#testaa järjestääkö ohjelma oikein
#esiintymistiheyden perusteella
#pienemmästä suurempaan
    def test_jarjestaminen(self):
        jarjestaminen = str(self.huffman.jarjestaminen())
        self.assertEqual(jarjestaminen,
        "[('t', 4), ('ä', 2), (' ', 2), ('e', 2), ('s', 2), ('i', 2), ('T', 1), \
('m', 1), ('o', 1), ('n', 1), ('k', 1), ('?', 1), ('!', 1), ('€', 1)]")
