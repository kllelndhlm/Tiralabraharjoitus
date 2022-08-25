from huffman import Huffman
from lzw import Lzw

def main():
    avauskysymys = input("Huffman vai LZW? (h/lzw)")

    if avauskysymys == "h":
        tiedostokysely = input("Mikä tiivistetään huffmanilla? (tiedostopolku)")
        with open(f"{tiedostokysely}", encoding="utf-8") as teksti:
            huffman = Huffman(teksti.read())
            Huffman.tiivistys(huffman)
            Huffman.purku(huffman)

    if avauskysymys == "lzw":
        tiedostokysely = input("Mikä tiivistetään LZW:llä? (tiedostopolku)")
        with open(f"{tiedostokysely}", encoding="utf-8") as teksti:
            lzw = Lzw(teksti.read())
            Lzw.pakkaus(lzw)
            Lzw.purkaus(lzw)

if __name__ == "__main__":
    main()
