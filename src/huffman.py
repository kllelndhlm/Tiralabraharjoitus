from huffman_alkio import Alkio

class Huffman:
    def __init__(self, teksti, tiedostopolku):
        self.teksti = teksti
        self.tiedostopolku = tiedostopolku
        self.pakattu_puu_pakattuun = ""

#luo kirjaston ja laskee pakattavan tekstin merkkien esiintymistiheydet
    def laske_esiintymistiheys(self):
        sanakirja = {}
        for i in self.teksti:
            if i not in sanakirja:
                sanakirja[i] = 1
            else:
                sanakirja[i] +=1
        return sanakirja

#luo kirjaston ja merkkejä vastaavat bittiesitykset
#bittiesityksellä tarkoitetaan tässä tapauksessa 1:iä ja 0:ia string-muodossa

    bittijonot = {}

    def luo_bittijonot(self, alkio, esitys = ""):
        uusi_esitys = esitys + f"{alkio.bitti}"
        if alkio.vasen:
            self.luo_bittijonot(alkio.vasen, uusi_esitys)
        if alkio.oikea:
            self.luo_bittijonot(alkio.oikea, uusi_esitys)
        if not alkio.oikea and not alkio.vasen:
            self.bittijonot[alkio.merkki] = uusi_esitys

#luo pakattavaa tekstiä vastaavan bittiesityksen
    pakattu_teksti = ""

    def luo_pakattu_teksti(self):
        bittijonoja_yhdistettavaksi = []
        for merkki in self.teksti:
            bittijonoja_yhdistettavaksi.append(self.bittijonot[merkki])
        self.pakattu_teksti = "".join(f"{k}" for k in bittijonoja_yhdistettavaksi)

#bittiesitys muutetaan kahdeksallajaolliseksi bytearrayta varten
    padding = 0
    bittivirta = ""

    def pakattu_kahdeksalla_jaollinen(self):
        self.padding = 8 - (len(self.pakattu_teksti) % 8)
        self.bittivirta = (self.padding * "0") + self.pakattu_teksti
        return self.bittivirta

#pakkaustiedoston kirjoittaminen bitteinä
#järjestyksessä kahdeksallajaollistamisen toppaus, puu, teskti
#erotusmerkkinä käytetty kolmea välilyöntiä
    def tallennus_bitteina(self):
        self.bittivirta = self.pakattu_kahdeksalla_jaollinen()
        tallenna = bytearray()

        for i in range(0, len(self.bittivirta), 8):
            tallenna.append(int(self.bittivirta[i:i + 8], 2))

        tiedostopolku_pakattuun = f"{self.tiedostopolku}".rsplit('.',1)[0] + "_huffman.bin"

        with open(tiedostopolku_pakattuun, "wb") as tiedosto:
            tiedosto.write(bytes(f"{self.padding}" + "   ", encoding="utf-8"))
            tiedosto.write(bytes(self.pakattu_puu_pakattuun, encoding="utf-8"))
            tiedosto.write(bytes(tallenna))

        return tiedostopolku_pakattuun

#luodaan puu, jolla pakkaus voidaan purkaa
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
        self.pakattu_puu_pakattuun = "".join(f"{k}" for k in self.puu_pakattuun) + "   "

#luo huffmanpuun alkiot
#palauttaa index.py'lle uuden tiedoston polun
    alkiot = []

    def pakkaus(self):
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

            uusi_alkio = Alkio(vasen.esiintymistiheys+oikea.esiintymistiheys,
vasen.merkki+oikea.merkki, vasen, oikea)
            self.alkiot.remove(vasen)
            self.alkiot.remove(oikea)
            self.alkiot.append(uusi_alkio)

        self.luo_bittijonot(self.alkiot[0])
        self.luo_pakattu_teksti()
        self.muunna_puu_pakattuun(self.alkiot[0])
        self.yhdista_puu_pakattuun_erotinmerkilla()
        polku = self.tallennus_bitteina()
        return polku

    def __str__(self):
        return f"{self.teksti}"

#Pohjana käytetty:
#https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328
#Lähteet:
#https://stackoverflow.com/questions/759707/efficient-way-of-storing-huffman-tree
