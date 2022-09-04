# Käyttöohje

## Asennus
Suorita komentorivillä
```bash
git clone https://github.com/kllelndhlm/Tiralabraharjoitus.git
```
Siirry tiedostoon komennolla
```bash
cd Tiralabraharjoitus/
```
Asenna ohjelma komennolla
```bash
poetry install
```

## Käyttö
Käynnistä ohjelma komennolla
```bash
poetry run invoke start
```
Valitse toiminto syöttämällä merkki(jono).

Huffman-pakkaus:
```bash
h
```
LZW-pakkaus:
```bash
lzw
```
Huffman-purku:
```bash
ph
```
LZW-purku:
```bash
plzw
```
Syötä käsiteltävä tiedoston tiedostopolku:<br>
esimerkiksi
```bash
testiteksti.txt
```

## Testaus
### Suorita testit
```bash
poetry run coverage run --branch -m pytest
```
### Testikattavuusraportti
```bash
poetry run invoke coverage-report
```
### Koodin laatu
```bash
poetry run invoke lint
```