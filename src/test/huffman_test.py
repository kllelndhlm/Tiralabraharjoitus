import unittest
from huffman import Huffman

class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.huffman = Huffman(open("../Tiralabraharjoitus/src/test/testiteksti.md").read()) #avaa testissä käytettävän tekstitiedoston

    def test_tulostus_oikein(self):
        tulostus = str(self.huffman)

        self.assertEqual(tulostus, "Tämä on testiteksti?!€")
