from huffman import Huffman

def main():
    avauskysymys = input("Tiivistetäänkö huffmanilla? (y/n)")  #KOKEILUA
    if avauskysymys == "n":  #KOKEILUA
        main()
    if avauskysymys == "y":  #KOKEILUA
        tiedostokysely = input("Mikä tiivistetään huffmanilla? (tiedostopolku)")  #KOKEILUA
        with open(f"{tiedostokysely}", encoding="utf-8") as teksti:
            huffman = Huffman(teksti.read())
            Huffman.tiivistys(huffman)
if __name__ == "__main__":
    main()
