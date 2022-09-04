# Testausdokumentti

## Yksikkötestauksen kattavuusraportti
![](https://raw.githubusercontent.com/kllelndhlm/Tiralabraharjoitus/main/Dokumentaatio/Kuvat/testikattavuus.jpg)

## Suorituskyvyn testaus

Algoritmien suorituskyky on testattu kuuden eri repositorion juuresta löytyvän materiaalin avulla:
* lyhyt teksti 8 B
* lyhyt pätkä toistuvia merkkejä 12 B
* lorem ipsum 1,1 kB
* toistuvia merkkejä 1,1 kB
* lorem ipsum 1,1 MB
* toistuvia merkkejä 1,1 MB

Suoritukseen kulunut aika on mitattu sijoittamalla suoritettavaan koodiin seuraavat rivit:<br>
* toiminnon importtaus:
```bash
import time
```
* mittauksen aloitus luokan luomisen yhteyteen:
```bash
self.aika = time.process_time()
```
* tulostus ennen funktion palautusta:
```bash
ajanotto = time.process_time() - self.aika
print(ajanotto) 
```
### Tulokset
Huffman
| sisältö | pakattava | pakattu | pakkaussuhde | aika | purun kesto |
|---|---|---|---|---|---|
|QQ\nWERTY| 8 B | 30 B | 375 % | 0,0005961589999999989 s | 0,0007719469999999985 s|
|101010101010|12 B|14 B|175 %|0,00043977600000000283 s| 0,0008575340000000001 s|
|lorem ipsum|1,1 kB|703 B|63,6 %|0,002750715000000001 s| 0,005389928999999998 s|
|1010...|1,1 kB|228 B|20,7%|0,0016327060000000011 s|0,003722872999999998 s|
|lorem ipsum|1 MB|536 kB|53,4 % %|0,325805524 s| 0,95710726 s|
|1010...|1 MB|193,4 kB|19,3 %|0,23805141 s| 0,6105789810000001 s|

Lempel-Ziv-Welch
| sisältö | pakattava | pakattu | pakkaussuhde | aika | purun kesto |
|---|---|---|---|---|---|
|QQ\nWERTY| 8 B | 32 b | 400 % | 0,000463245000000001 s | 0,0005196699999999999 s|
|101010101010|12 B| 35 B| 291,7 %|0,0005102849999999992 s|0,0006910679999999995 s|
|lorem ipsum|1,1 kB|1,6 kB| 142,5 %|0,0019036910000000025 s|0,0017957639999999983 s|
|1010...|1,1 kB| 390 B|35,5 %|0,0012743390000000028 s| 0,0009365240000000011 s |
|lorem ipsum|1 MB|432,4 kB|43,1 % %|0,213481021 s| 0,11237909200000001 s|
|1010...|1 MB| 14,0 kB|1,4 %| 0,199034942 s| 0,018339670000000002 s |

Tulosten perusteella pienten tiedostojen pakkaus on ilmeisen turhaa. Huffman alkaa toimimaan positiivisella tavalla pienemmissä tiedostoissa aiemmin kuin Lempel-Ziv-Welch. Lempel-Ziv-Welch alkaa tiedostojen suuretessa osoittaa paremmuutensa pakkaussuhteen parantuessa. Huffmanin suoritusaika pitenee huomattavasti tiedostojen kasvaessa, toisin kuin tasaisempi Lempel-Ziv-Welch. Tämän perusteella toteutukset ovat ainakin lähelle tavoiteltuja aikavaativuuksiaan, Huffmanillä O(n log n) ja Lempel-Ziv-Welchillä O(n).