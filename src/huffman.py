class Huffman:
    def __init__(self, teksti):
        self.teksti = teksti

    def esiintymistiheys(self):
        sanakirja = dict()
        for i in self.teksti:
            if i not in sanakirja:
                sanakirja[i] = 1
            else:
                sanakirja[i] +=1

        return sanakirja

    def __str__(self):
        return f"{self.teksti}" 

