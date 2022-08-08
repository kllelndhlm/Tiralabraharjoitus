class Huffman:
    def __init__(self, teksti):
        self.teksti = teksti

    def esiintymistiheys(self):
        sanakirja = {}

        for i in self.teksti:
            if i not in sanakirja:
                sanakirja[i] = 1
            else:
                sanakirja[i] +=1

        return sanakirja

    def jarjestaminen(self):
        sanakirja = self.esiintymistiheys()

        jarjestetty_sanakirja = sorted(sanakirja.items(), key=lambda x: x[1], reverse=True)

        return jarjestetty_sanakirja

    def __str__(self):
        return f"{self.teksti}"
