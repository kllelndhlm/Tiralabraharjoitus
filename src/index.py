import os
from huffman import Huffman
from lzw import Lzw

def main():
    avauskysymys = input("Pakkaus: Huffman tai LZW? (h/lzw)\nVai purku: Huffman tai LZW? (ph/plzw)")

    if avauskysymys == "h":
        tiedostokysely = input("Mitä tiivistetään huffmanilla? (tiedostopolku)")
        with open(f"{tiedostokysely}", encoding="utf-8") as teksti:
            huffman = Huffman(teksti.read(), tiedostokysely)
            Huffman.tiivistys(huffman)

    if avauskysymys == "lzw":
        tiedostokysely = input("Mitä tiivistetään LZW:llä? (tiedostopolku)")
        with open(f"{tiedostokysely}", encoding="utf-8") as teksti:
            data = teksti.read()
            lzw = Lzw(data, tiedostokysely)
            Lzw.pakkaus(lzw)

    if avauskysymys == "ph":
        tiedostokysely = input("Mitä puretaan huffmanilla? (tiedostopolku)")
        with open(f"{tiedostokysely}", "rb") as teksti:
            data = teksti.read()
            huffman = Huffman(data, tiedostokysely)
            huffman.purku()

    if avauskysymys == "plzw":
        tiedostokysely = input("Mikä puretaan LZW:llä? (tiedostopolku)")
        with open(f"{tiedostokysely}", "rb") as teksti:
            data = teksti.read()
            lzw = Lzw(data, tiedostokysely)
            Lzw.purkaus(lzw)

if __name__ == "__main__":
    main()
