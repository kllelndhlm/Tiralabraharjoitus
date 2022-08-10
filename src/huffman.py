from huffman_alkio import Alkio

class Huffman:
    def __init__(self, teksti):
        self.teksti = teksti
        self.alkiot = []
        self.sanakirja = {}

    def esiintymistiheys(self):
        for i in self.teksti:
            if i not in self.sanakirja:
                self.sanakirja[i] = 1
            else:
                self.sanakirja[i] +=1
        return self.sanakirja

    def jarjestaminen(self):
        sanakirja = self.esiintymistiheys()
        jarjestetty_sanakirja = sorted(sanakirja.items(), key=lambda x: x[1])
        return jarjestetty_sanakirja

    def luo_alkiot(self):
        merkkiarvoparit = self.sanakirja
        for key, value in merkkiarvoparit.items():
            self.alkiot.append(Alkio(key, value))

    def tiivistys(self):
        self.esiintymistiheys()
        self.luo_alkiot()

    def __str__(self):
        return f"{self.teksti}"
