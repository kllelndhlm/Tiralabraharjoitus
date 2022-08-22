from huffman_alkio import Alkio

class Huffman:
    def __init__(self, teksti):
        self.teksti = teksti
        self.alkiot = []
        self.bittijonot = {}
        self.tiivistetty_teksti = ""
        self.padding = 0
        self.binaariksi = ""
        self.bittivirta = ""
        self.puu_pakattuun = []
        self.tiivistetty_puu_pakattuun = ""

    def laske_esiintymistiheys(self):
        sanakirja = dict()
        for i in self.teksti:
            if i not in sanakirja:
                sanakirja[i] = 1
            else:
                sanakirja[i] +=1
        jarjestetty_sanakirja = dict(sorted(sanakirja.items(), key=lambda x: x[1], reverse=True))
        return jarjestetty_sanakirja

    def jarjesta_alkiot(self):
        self.alkiot = sorted(self.alkiot, key=lambda x: x.esiintymistiheys)

    def luo_bittijonot(self, alkio, esitys = ""):
        uusi_esitys = esitys + f"{alkio.bitti}"
        if alkio.vasen_lapsi:
            self.luo_bittijonot(alkio.vasen_lapsi, uusi_esitys)
        if alkio.oikea_lapsi:
            self.luo_bittijonot(alkio.oikea_lapsi, uusi_esitys)
        if not alkio.oikea_lapsi and not alkio.vasen_lapsi:
            self.bittijonot[alkio.merkki] = uusi_esitys

    def luo_tiivistetty_teksti(self):
        bittijonoja_yhdistettavaksi = []
        for merkki in self.teksti:
            bittijonoja_yhdistettavaksi.append(self.bittijonot[merkki])
        self.tiivistetty_teksti = "".join(f"{k}" for k in bittijonoja_yhdistettavaksi)

    def tiivistetty_kahdeksalla_jaollinen(self):
        self.padding = 8 - (len(self.tiivistetty_teksti) % 8)
        self.bittivirta = (self.padding * "0") + self.tiivistetty_teksti
        return self.bittivirta

    def tallennus_bitteina(self):
        self.bittivirta = self.tiivistetty_kahdeksalla_jaollinen()
        tallenna = bytearray()
        for i in range(0, len(self.bittivirta), 8):
            tallenna.append(int(self.bittivirta[i:i + 8], 2))
        with open("../Tiralabraharjoitus/src/test/testitallennus.bin", "wb") as f:
            f.write(bytes(self.tiivistetty_puu_pakattuun, encoding="utf-8"))
            f.write(bytes(tallenna))

    def muunna_puu_pakattuun(self, alkio):
        if alkio.vasen_lapsi is None and alkio.oikea_lapsi is None:
            self.puu_pakattuun.append(1)
            self.puu_pakattuun.append(alkio.merkki)
        else:
            self.puu_pakattuun.append(0)
            self.muunna_puu_pakattuun(alkio.oikea_lapsi)
            self.muunna_puu_pakattuun(alkio.vasen_lapsi)

    def yhdista_puu_pakattuun_erotinmerkilla(self):
        self.tiivistetty_puu_pakattuun = "".join(f"{k}" for k in self.puu_pakattuun) + "   "
        print(self.tiivistetty_puu_pakattuun)

    def avaa_pakattu(self):
        pass

    def pura_pakattu(self):
        pass

    def tallenna_purettu(self):
        pass

    def tiivistys(self):
        merkkiarvoparit = self.laske_esiintymistiheys()
        merkit = merkkiarvoparit.keys()

        for merkki in merkit:
            self.alkiot.append(Alkio(merkkiarvoparit[merkki], merkki))        

        while len(self.alkiot) > 1:
            self.jarjesta_alkiot()
            oikea_alkio = self.alkiot[0]
            vasen_alkio = self.alkiot[1]
            vasen_alkio.bitti = 0
            oikea_alkio.bitti = 1
            uusi_alkio = Alkio(vasen_alkio.esiintymistiheys+oikea_alkio.esiintymistiheys, vasen_alkio.merkki+oikea_alkio.merkki, vasen_alkio, oikea_alkio)
            self.alkiot.remove(vasen_alkio)
            self.alkiot.remove(oikea_alkio)
            self.alkiot.append(uusi_alkio)

        self.luo_bittijonot(self.alkiot[0])
        self.luo_tiivistetty_teksti()
        self.muunna_puu_pakattuun(self.alkiot[0])
        self.yhdista_puu_pakattuun_erotinmerkilla()
        self.tallennus_bitteina()

    def purku(self):
        self.avaa_pakattu()
        self.pura_pakattu()
        self.tallenna_purettu()

    def __str__(self):
        return f"{self.teksti}"
