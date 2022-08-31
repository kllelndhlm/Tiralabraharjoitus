import pickle

class Lzw:
    def __init__(self, teksti, tiedostopolku):
        self.teksti = teksti
        self.tiedostopolku = tiedostopolku
        self.sanakirjan_koko = 256
        self.sanakirja = []

    def pakkaus(self):
        self.sanakirja = {chr(i): i for i in range(self.sanakirjan_koko)}
        merkkijono = ""
        pakatut_merkit = []

        for merkki in self.teksti:
            merkkijono_ja_merkki = merkkijono + merkki
            if merkkijono_ja_merkki in self.sanakirja:
                merkkijono = merkkijono_ja_merkki
            else:
                pakatut_merkit.append(self.sanakirja[merkkijono])
                self.sanakirja[merkkijono_ja_merkki] = self.sanakirjan_koko
                self.sanakirjan_koko += 1
                merkkijono = merkki

        if merkkijono in self.sanakirja:
            pakatut_merkit.append(self.sanakirja[merkkijono])

        paketti_tiedostoon =  bytearray(pickle.dumps(pakatut_merkit))
        tiedostonnimi = f"{self.tiedostopolku}".rsplit('.',1)[0]
        polku_tiedostoon = tiedostonnimi + "_LZW.bin"
        with open(polku_tiedostoon, 'wb') as tiedosto:
            tiedosto.write(paketti_tiedostoon)
        return polku_tiedostoon

#Pohjana käytetty:
#https://github.com/adityagupta3006/LZW-Compressor-in-Python/blob/master/encoder.py
#Lähteet:https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
#https://rosettacode.org/wiki/LZW_compression#Python
