import pickle
import struct
from struct import *

class Lzw:
    def __init__(self, teksti):
        self.teksti = teksti
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
        
        tiedostoon =  bytearray(pickle.dumps(pakatut_merkit))
        with open("../Tiralabraharjoitus/src/test/testipakkausLZW.bin", 'wb') as f:
            f.write(tiedostoon)

    def purkaus(self):
        self.sanakirja = {i: chr(i) for i in range(self.sanakirjan_koko)}
        purettava = pickle.loads(self.teksti)
        print(self.sanakirja)
        seuraava_koodi = 256
        merkkijono = ""
        purettu = ""

###<TESTING>
        merkkijono = str(purettava.pop(0))
        purettu = purettu + merkkijono
        for merkki in purettava:
            print(merkki)
            if merkki in self.sanakirja:
                kirjoita = self.sanakirja[merkki]
                purettu = purettu + kirjoita

            elif merkki == self.sanakirjan_koko:
                kirjoita = merkkijono + merkkijono[0]
                purettu = purettu + kirjoita

            self.sanakirja[self.sanakirjan_koko] = merkkijono + kirjoita[0]
            self.sanakirjan_koko += 1
     
            merkkijono = kirjoita


###</TESTING>

#        for koodi in purettava:
#            if not (koodi in self.sanakirja):
#                self.sanakirja[koodi] = merkkijono + (merkkijono[0])
#            purettu += self.sanakirja[koodi]
#            if not(len(merkkijono) == 0):
#                self.sanakirja[seuraava_koodi] = merkkijono + (self.sanakirja[koodi][0])
#                seuraava_koodi += 1
#            merkkijono = self.sanakirja[koodi]

        with open("../Tiralabraharjoitus/src/test/testipurkausLZW.txt", 'w') as f:
            f.write(purettu)


#Pohjana käytetty: https://github.com/adityagupta3006/LZW-Compressor-in-Python/blob/master/encoder.py
#Lähteet: https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch