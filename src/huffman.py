from huffman_alkio import Alkio

class Huffman:
    def __init__(self, teksti, tiedostopolku):
        self.teksti = teksti
        self.alkiot = []
        self.bittijonot = {}
        self.tiivistetty_teksti = ""
        self.padding = 0
        self.binaariksi = ""
        self.bittivirta = ""
        self.tiivistetty_puu_pakattuun = ""
        self.purun_padding = 0
        self.purun_puu = ""
        self.puu_alku = 0
        self.puu_leikkaamaton = ""
        self.puu_loppu = 0
        self.purettu_puu_pakattu = ""
        self.koodattu_teksti = []
        self.puretut_alkiot = []
        self.purettu_bittivirta = ""
        self.purettu_puu = ""
        self.tiedostopolku = tiedostopolku

    def laske_esiintymistiheys(self):
        sanakirja = {}
        for i in self.teksti:
            if i not in sanakirja:
                sanakirja[i] = 1
            else:
                sanakirja[i] +=1
        return sanakirja

    def luo_bittijonot(self, alkio, esitys = ""):
        uusi_esitys = esitys + f"{alkio.bitti}"
        if alkio.vasen:
            self.luo_bittijonot(alkio.vasen, uusi_esitys)
        if alkio.oikea:
            self.luo_bittijonot(alkio.oikea, uusi_esitys)
        if not alkio.oikea and not alkio.vasen:
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
        tiedostonnimi = f"{self.tiedostopolku}".rsplit('.',1)[0]
        polku_tiedostoon = tiedostonnimi + "_huffman.bin"
        with open(polku_tiedostoon, "wb") as f:
            f.write(bytes(f"{self.padding}" + "   ", encoding="utf-8"))
            f.write(bytes(self.tiivistetty_puu_pakattuun, encoding="utf-8"))
            f.write(bytes(tallenna))

    puu_pakattuun = []

    def muunna_puu_pakattuun(self, alkio):
        if alkio.vasen is None and alkio.oikea is None:
            self.puu_pakattuun.append(1)
            self.puu_pakattuun.append(alkio.merkki)
        else:
            self.puu_pakattuun.append(0)
            self.muunna_puu_pakattuun(alkio.vasen)
            self.muunna_puu_pakattuun(alkio.oikea)


    def yhdista_puu_pakattuun_erotinmerkilla(self):
        self.tiivistetty_puu_pakattuun = "".join(f"{k}" for k in self.puu_pakattuun) + "   "

    def avaa_pakattu(self):
        with open(f"{self.tiedostopolku}", "rb") as bitit:
            lue_bitit = bitit.read()
            self.purun_padding = int(f"{lue_bitit}"[2])
            self.puu_alku = 6
            self.puu_leikkaamaton = str(lue_bitit)[self.puu_alku:]
            for i in range(len(self.puu_leikkaamaton)):
                if self.puu_leikkaamaton[i+1:i+4] == "   ":
                    self.puu_loppu = i+1
                    break
            self.purettu_puu_pakattu = self.puu_leikkaamaton[:self.puu_loppu]
            kaikki_bitit = ''.join(format(byte, '08b') for byte in lue_bitit)
        with open(f"{self.tiedostopolku}", "rb") as bitit2:
            lue_tekstia_edeltavat_bitit = bitit2.read(self.puu_loppu+6)
            bitit_ennen_tekstia = ''.join(format(byte, '08b') for byte in lue_tekstia_edeltavat_bitit)
            self.purettu_bittivirta = kaikki_bitit[len(bitit_ennen_tekstia) + self.purun_padding:]
            self.koodattu_teksti = self.puu_leikkaamaton[self.puu_loppu + 3:-1]

    def pura_pakattu_puu(self):
        with open(f"{self.tiedostopolku}", "rb") as bitit3:
            bitit_puuhun = bitit3.read(self.puu_loppu+3)      
        for i in range(len(bitit_puuhun)):
            merkki = bitit_puuhun[i:i+1].decode("utf-8")
            self.purettu_puu = self.purettu_puu + merkki
        self.purettu_puu = self.purettu_puu[4:]
        return self.purettu_puu

    i = 0

    def luo_purkupuu(self, puukoodi):
        if puukoodi[self.i] == "1":
            self.i += 1
            uusi_alkio = Alkio(0, puukoodi[self.i])
            self.puretut_alkiot.append(uusi_alkio)

        else:
            self.i += 1
            vasen = self.luo_purkupuu(puukoodi)
            self.i += 1
            oikea= self.luo_purkupuu(puukoodi)
            uusi_alkio = Alkio(0, "0", vasen, oikea)
            self.puretut_alkiot.append(uusi_alkio)

        return uusi_alkio

    def tiivistys(self):
        merkkiarvoparit = self.laske_esiintymistiheys()
        merkit = merkkiarvoparit.keys()
    
        for merkki in merkit:
            self.alkiot.append(Alkio(merkkiarvoparit.get(merkki), merkki))

        while len(self.alkiot) > 1:
            self.alkiot = sorted(self.alkiot, key=lambda x: x.esiintymistiheys)
            oikea = self.alkiot[0]
            vasen = self.alkiot[1]
            vasen.bitti = 0
            oikea.bitti = 1
            uusi_alkio = Alkio(vasen.esiintymistiheys+oikea.esiintymistiheys, vasen.merkki+oikea.merkki, vasen, oikea)
            self.alkiot.remove(vasen)
            self.alkiot.remove(oikea)
            self.alkiot.append(uusi_alkio)
        self.luo_bittijonot(self.alkiot[0])
        self.luo_tiivistetty_teksti()
        self.muunna_puu_pakattuun(self.alkiot[0])
        self.yhdista_puu_pakattuun_erotinmerkilla()
        self.tallennus_bitteina()

    def purku(self):
        self.avaa_pakattu()
        puukoodi = self.pura_pakattu_puu()
        purkupuu = self.luo_purkupuu(puukoodi)
        alku = purkupuu
        purettu_teksti = []
        for x in self.purettu_bittivirta:
            if x == '1':
                purkupuu = purkupuu.oikea   
            elif x == '0':
                purkupuu = purkupuu.vasen
            try:
                if purkupuu.vasen.merkki == None and purkupuu.oikea.merkki == None:
                    pass
            except AttributeError:
                purettu_teksti.append(purkupuu.merkki)
                purkupuu = alku

        teksti = ''.join([str(item) for item in purettu_teksti])

        tiedostonnimi = f"{self.tiedostopolku}".rsplit('.',1)[0]
        polku_tiedostoon = tiedostonnimi + "_huffman_purettu.txt"
        with open(polku_tiedostoon, 'w') as f:
            f.write(teksti)

    def __str__(self):
        return f"{self.teksti}"

#Pohjana käytetty: https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328
#Lähteet: https://stackoverflow.com/questions/759707/efficient-way-of-storing-huffman-tree