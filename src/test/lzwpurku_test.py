import unittest
from lzw_purku import Lzwpurku

#avaa testissä käytettävän tekstitiedoston
class TestLzwpurku(unittest.TestCase):
    def setUp(self):
        self.lzw_purku = Lzwpurku(
b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00]\x94(KQKQK\nKWKEKRKTKYe.',
"../Tiralabraharjoitus/testiteksti_LZW.bin")

    def test_purku(self):
        purku = f"{self.lzw_purku.purku()}"
        self.assertEqual(purku, "../Tiralabraharjoitus/testiteksti_LZW_purettu.txt")
