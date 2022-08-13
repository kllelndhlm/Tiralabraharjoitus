from huffman import Huffman

def main():
    avauskysymys = input("Tiivistetäänkö huffmanilla? (y/n)")
    if avauskysymys == "n":
        main()
    if avauskysymys == "y":
        tiedostokysely = input("Mikä tiivistetään huffmanilla? (tiedostopolku)")
        with open(f"{tiedostokysely}", encoding="utf-8") as teksti:
            huffman = Huffman(teksti.read())
            Huffman.tiivistys(huffman)
            Huffman.purku(huffman)
if __name__ == "__main__":
    main()
