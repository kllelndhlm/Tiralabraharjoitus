import pickle

class Lzwpurku:
    def __init__(self, teksti, tiedostopolku):
        self.teksti = teksti
        self.tiedostopolku = tiedostopolku
        self.sanakirjan_koko = 256
        self.sanakirja = []

#luo sanakirjan kaikista merkeistä
#laajentaa sanakirjaa ja purkaa pakatun tekstin
    def purku(self):
        self.sanakirja = {i: chr(i) for i in range(self.sanakirjan_koko)}
        purettava = pickle.loads(self.teksti)
        seuraava_koodi = 256
        merkkijono = ""
        purettu = ""

        for koodi in purettava:
            if not koodi in self.sanakirja:
                self.sanakirja[koodi] = merkkijono + (merkkijono[0])
            purettu += self.sanakirja[koodi]
            if len(merkkijono) != 0:
                self.sanakirja[seuraava_koodi] = merkkijono + (self.sanakirja[koodi][0])
                seuraava_koodi += 1
            merkkijono = self.sanakirja[koodi]

        tiedostonnimi = f"{self.tiedostopolku}".rsplit('.',1)[0]
        polku_tiedostoon = tiedostonnimi + "_purettu.txt"
        with open(polku_tiedostoon, 'w', encoding="utf-8") as tiedosto:
            tiedosto.write(purettu)
        return polku_tiedostoon

#Pohjana käytetty:
#https://github.com/adityagupta3006/LZW-Compressor-in-Python/blob/master/encoder.py
#Lähteet:
#https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
#https://rosettacode.org/wiki/LZW_compression#Python
