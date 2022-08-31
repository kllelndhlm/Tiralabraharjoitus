import os
from huffman import Huffman
from huffman_purku import Huffmanpurku
from lzw import Lzw
from lzw_purku import Lzwpurku

def main():
    avauskysymys = input(
"Pakkaus: Huffman tai LZW? (h/lzw)\nVai purku: Huffman tai LZW? (ph/plzw)\n")

    if avauskysymys == "h":
        tiedostokysely = input("Mitä pakataan huffmanilla? (tiedostopolku)\n")
        with open(f"{tiedostokysely}", encoding="utf-8") as teksti:
            huffman = Huffman(teksti.read(), tiedostokysely)
            pakkaus = Huffman.pakkaus(huffman)
            print("Pakattu tiedosto kohteessa", pakkaus,
"\nAlkuperäinen koko:", round((os.path.getsize(tiedostokysely) / 1000), 1), "kB",
"\nPakatun koko:", round((os.path.getsize(pakkaus) / 1000), 1), "kB",
"\nPakkaussuhde:", round((os.path.getsize(pakkaus)
/ (os.path.getsize(tiedostokysely)) * 100), 1), "%")

    if avauskysymys == "lzw":
        tiedostokysely = input("Mitä pakataan LZW:llä? (tiedostopolku)\n")
        with open(f"{tiedostokysely}", encoding="utf-8") as teksti:
            data = teksti.read()
            lzw = Lzw(data, tiedostokysely)
            pakkaus = Lzw.pakkaus(lzw)
            print("Pakattu tiedosto kohteessa", pakkaus,
"\nAlkuperäinen koko:", round((os.path.getsize(tiedostokysely) / 1000), 1), "kB",
"\nPakatun koko:", round((os.path.getsize(pakkaus) / 1000), 1), "kB",
"\nPakkaussuhde:", round((os.path.getsize(pakkaus)
/ (os.path.getsize(tiedostokysely)) * 100), 1), "%")

    if avauskysymys == "ph":
        tiedostokysely = input("Mitä puretaan huffmanilla? (tiedostopolku)\n")
        with open(f"{tiedostokysely}", "rb") as teksti:
            data = teksti.read()
            huffman_purku = Huffmanpurku(data, tiedostokysely)
            purku = Huffmanpurku.purku(huffman_purku)
            with open(f"{tiedostokysely}"[:-12]+".txt", encoding="utf-8") as teksti:
                alkup_teksti = teksti.read()
            with open(f"{purku}", encoding="utf-8") as teksti:
                purettu_teksti = teksti.read()
            print("Purettu tiedosto kohteessa", purku,
"\nAlkuperäinen teksti:\n", alkup_teksti[:100], "jne.",
"\nPaketista purettu teksti:\n", purettu_teksti[:100], "jne."
"\nPurettu vastaa alkuperäistä:", purettu_teksti == alkup_teksti)

    if avauskysymys == "plzw":
        tiedostokysely = input("Mikä puretaan LZW:llä? (tiedostopolku)\n")
        with open(f"{tiedostokysely}", "rb") as teksti:
            data = teksti.read()
            lzw_purku = Lzwpurku(data, tiedostokysely)
            purku = Lzwpurku.purku(lzw_purku)
            with open(f"{tiedostokysely}"[:-8]+".txt", encoding="utf-8") as teksti:
                alkup_teksti = teksti.read()
            with open(f"{purku}", encoding="utf-8") as teksti:
                purettu_teksti = teksti.read()
            print("Purettu tiedosto kohteessa", purku,
"\nAlkuperäinen teksti:\n", alkup_teksti[:100], "jne.",
"\nPaketista purettu teksti:\n", purettu_teksti[:100], "jne."
"\nPurettu vastaa alkuperäistä:", purettu_teksti == alkup_teksti)

if __name__ == "__main__":
    main()
