import unittest
from huffman_purku import Huffmanpurku

#avaa testissä käytettävän tekstitiedoston
class TestHuffmanpurku(unittest.TestCase):
    def setUp(self):
        self.huffman_purku = Huffmanpurku("b'2   0001Y1T01R1E001W1\n1Q   >\xc6\x88'",
"../Tiralabraharjoitus/testiteksti_huffman.bin")

#testaa avaako ohjelma oikean tiedoston
    def test_tulostus_oikein(self):
        tulostus = f"{self.huffman_purku}"
        self.assertEqual(tulostus, "b'2   0001Y1T01R1E001W1\n1Q   >\xc6\x88'")

#testaa toimiiko pakkauksen avaaminen erotinmerkillä
    def test_avaa_pakattu(self):
        avaa_pakattu = f"{self.huffman_purku.avaa_pakattu()}"
        self.assertEqual(avaa_pakattu, "(21, '1111101100011010001000')")

#testaa luodaanko purkuun tarvittavien alkioiden luonti
#alkioiden tunnisteet eivät ole joka kerta samankaltaisia
#testaa vain palauttaako funktio alkioita
    def test_luo_purkupuu(self, puukoodi="0001g1F01e1d001c1b01a0001t001k1/1i1G01\n001s1x1."):
        luo_purkupuu = str(self.huffman_purku.luo_purkupuu(puukoodi))[:31]
        self.assertEqual(luo_purkupuu, "<huffman_alkio.Alkio object at ")

#testaa pakatun puun purku
    def test_pura_pakattu_puu(self, puu_loppu=21):
        pura_pakattu_puu = f"{self.huffman_purku.pura_pakattu_puu(puu_loppu)}"
        self.assertEqual(pura_pakattu_puu, "0001Y1T01R1E001W1\n1Q")

#testaa palautetaanko oikea tiedostopolku
    def test_purku(self):
        purku = f"{self.huffman_purku.purku()}"
        self.assertEqual(purku, "../Tiralabraharjoitus/testiteksti_huffman_purettu.txt")
