from huffman_alkio import Alkio

class Huffmanpurku:
    def __init__(self, teksti, tiedostopolku):
        self.teksti = teksti
        self.tiedostopolku = tiedostopolku

#laskee koodatun huffman-puun sijainnin pakkauksessa ja avaa pakatun tekstin
    def avaa_pakattu(self):
        puu_loppu = 0

        with open(f"{self.tiedostopolku}", "rb") as bitit:
            lue_bitit = bitit.read()
            puu_leikkaamaton = str(lue_bitit)[6:] #Puu alkaa indeksistä 6
            for i in range(len(puu_leikkaamaton)):
                if puu_leikkaamaton[i+1:i+4] == "   ": #Puu päättyy erotinmerkkiin "   "
                    puu_loppu = i+1
                    break

            kaikki_bitit = ''.join(format(byte, '08b') for byte in lue_bitit)

        with open(f"{self.tiedostopolku}", "rb") as bitit2:
            lue_tekstia_edeltavat_bitit = bitit2.read(puu_loppu+6)
            bitit_ennen_tekstia = ''.join(format(byte, '08b')
for byte in lue_tekstia_edeltavat_bitit)
            purettu_bittivirta = kaikki_bitit[len(bitit_ennen_tekstia)
+ int(f"{lue_bitit}"[2]):]
        return puu_loppu, purettu_bittivirta

#purkaa huffman-puun
    def pura_pakattu_puu(self, puu_loppu):
        purettu_puu = ""
        with open(f"{self.tiedostopolku}", "rb") as bitit3:
            bitit_puuhun = bitit3.read(puu_loppu+3)
        for i in range(len(bitit_puuhun)):
            merkki = bitit_puuhun[i:i+1].decode("utf-8")
            purettu_puu = purettu_puu + merkki
        purettu_puu = purettu_puu[4:]
        print(purettu_puu)
        return purettu_puu

#luo huffman-alkiot tekstin purkamista varten
    i = 0

    def luo_purkupuu(self, puukoodi):
        if puukoodi[self.i] == "1":
            self.i += 1
            uusi_alkio = Alkio(0, puukoodi[self.i])

        else:
            self.i += 1
            vasen = self.luo_purkupuu(puukoodi)
            self.i += 1
            oikea= self.luo_purkupuu(puukoodi)
            uusi_alkio = Alkio(0, "0", vasen, oikea)
        return uusi_alkio

#purkaa pakkauksen seuraamalla huffman-puuta
#palauttaa index.py'lle uuden tiedoston polun
    def purku(self):
        puu_loppu, purettu_bittivirta = self.avaa_pakattu()
        puukoodi = self.pura_pakattu_puu(puu_loppu)
        purkupuu = self.luo_purkupuu(puukoodi)
        alku = purkupuu
        purettu_teksti = []
        for bitti in purettu_bittivirta:
            if bitti == '1':
                purkupuu = purkupuu.oikea
            elif bitti == '0':
                purkupuu = purkupuu.vasen
            try:
                if purkupuu.vasen.merkki is None and purkupuu.oikea.merkki is None:
                    pass
            except AttributeError:
                purettu_teksti.append(purkupuu.merkki)
                purkupuu = alku

        teksti = ''.join([str(item) for item in purettu_teksti])

        tiedostonnimi = f"{self.tiedostopolku}".rsplit('.',1)[0]
        polku_tiedostoon = tiedostonnimi + "_purettu.txt"
        with open(polku_tiedostoon, 'w', encoding="utf-8") as tiedosto:
            tiedosto.write(teksti)
        return polku_tiedostoon

    def __str__(self):
        return f"{self.teksti}"

#Pohjana käytetty:
#https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328
#Lähteet:
#https://stackoverflow.com/questions/759707/efficient-way-of-storing-huffman-tree
