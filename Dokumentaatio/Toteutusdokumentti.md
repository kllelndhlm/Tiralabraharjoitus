# Toteutusdokumentti

## Ohjelman yleisrakenna

### Käyttöliittymä

Ohjelman käyttöliittymä toimii komentoriviltä. Käyttöliittymän käynnistää index.py. Käyttäjän ilmoittamaa ohjelman osaa kutsutaan argumenteilla tiedostopolku ja polusta luettu data. Vastauksena palautuu uuden tiedoston polku. Komentoriville tulostuu polku ja vertailu ohjelman toimivuudesta.

### Huffman

Huffman-pakkaus luo tekstistä alkioita ja alkioista huffman-puun. Puun avulla teksti pakataan ja tallennetaan bitteinä. Pakattu teksti puretaan kulkemalla pakkaustiedostosta purettua huffman-puuta takaisin.

### Lempel-Ziv-Welch

Lempel-Ziv-Welch-pakkaus luo sanakirjan kaikista merkeistä ja etsii tekstistä mahdollisia pidempiä toistuvia merkkijonoja. Löydetyt lisätään kirjastoon. Purettaessa kirjasto luodaan uudelleen ja teksti käännetään sen avula.

## Saavutetut aika- ja tilavaativuudet

* Huffman-pakkaus: O(n log n)
* Huffman-purku: O(n log n)
* Lempel-Ziv-Welch-pakkaus: O(n)
* Lempel-Ziv-Welch-purku: O(n)

Huffmanin ja Lempel-Ziv-Welchin vertailua enemmän testausdokumentissa.

## Puutteet ja parannusehdotukset

Ohjelma ei toimi joidenkin erikois- ja skandimerkkien kanssa. Pakkaus menisi vielä tiiviimmäksi, jos käyttäisi bytearrayn sijaan bitarrayta.