from huffman_alkio import Alkio

class Huffman:
    def __init__(self, teksti):
        self.teksti = teksti
        self.alkiot = []
        self.sanakirja = {}
        self.bittijonot = {}
        self.tiivistetty_teksti = ""
        self.padding = 0

    def laske_esiintymistiheys(self):
        for i in self.teksti:
            if i not in self.sanakirja:
                self.sanakirja[i] = 1
            else:
                self.sanakirja[i] +=1
        return self.sanakirja

    def jarjestaminen(self):
        self.alkiot = sorted(self.alkiot, key=lambda x: x.esiintymistiheys)

    def luo_alkiot(self):
        merkkiarvoparit = self.sanakirja
        for key, value in merkkiarvoparit.items():
            self.alkiot.append(Alkio(key, value))

    def luo_puu(self):
        while len(self.alkiot) > 1:
            self.jarjestaminen()
            oikea_alkio = self.alkiot[0]
            vasen_alkio = self.alkiot[1]
            oikea_alkio.bitti = 1
            vasen_alkio.bitti = 0
            uusi_alkio = Alkio(oikea_alkio.merkki+vasen_alkio.merkki, oikea_alkio.esiintymistiheys+vasen_alkio.esiintymistiheys, oikea_alkio, vasen_alkio)
            self.alkiot.remove(oikea_alkio)
            self.alkiot.remove(vasen_alkio)
            self.alkiot.append(uusi_alkio)

    def luo_bittijonot(self, alkio, esitys = ""):
        uusi_esitys = esitys + f"{alkio.bitti}"
        if alkio.oikea_lapsi:
            self.luo_bittijonot(alkio.oikea_lapsi, uusi_esitys)
        if alkio.vasen_lapsi:
            self.luo_bittijonot(alkio.vasen_lapsi, uusi_esitys)
        if not alkio.oikea_lapsi and not alkio.vasen_lapsi:
            self.bittijonot[alkio.merkki] = uusi_esitys

    def luo_tiivistetty_teksti(self):
        bittijonoja_yhdistettavaksi = []
        for m in self.teksti:
            bittijonoja_yhdistettavaksi.append(self.bittijonot[m])
        self.tiivistetty_teksti = "".join(f"{k}" for k in bittijonoja_yhdistettavaksi)

    def tiivistetty_on_kahdeksalla_jaollinen(self):
        if len(self.tiivistetty_teksti) % 8 != 0:
            self.padding = 8 - (len(self.tiivistetty_teksti) % 8)
            binaariksi = self.padding * "0" + self.tiivistetty_teksti
        else:
            binaariksi = self.tiivistetty_teksti
        bittivirta = bytearray(int(binaariksi[x:x+8], 2) for x in range(0, len(binaariksi), 8))
        with open("../Tiralabraharjoitus/src/test/testitallennus.txt", "wb") as f:
            f.write(bittivirta)

    def tiivistys(self):
        self.laske_esiintymistiheys()
        self.luo_alkiot()
        self.luo_puu()
        self.luo_bittijonot(self.alkiot[0])
        self.luo_tiivistetty_teksti()
        self.tiivistetty_on_kahdeksalla_jaollinen()

    def __str__(self):
        return f"{self.teksti}"
