# Testausdokumentti

## Automaattitestit

Automaattitestit on määritelty hakemistossa [`src/tests`](/src/tests).

Testit käyttävät `pytest` ja `unittest` -kirjastoja, ja niissä hyödynnetään
riippuvuuksien injektointeja sekä stub/mock-toteutuksia tarpeen mukaan, jotta ne
eivät riippuisi turhaan muista komponenteista.

### Pelilogiikka

Merkittävin testattu komponentti on pelilogiikasta vastaava `PlayService`. Testit
kokeilevat kattavasti erilaisia pelin tilanteita.

`PlayService` käyttää satunnaisuutta järjestämään tekstit ja kuvat. Testejä
varten Pythonin `shuffle` korvataan riippuvuuden injektoinnilla `setUp`-
vaiheessa vakiosiemenellä alustetulla satunnaisluokalla. Tällöin palvelu
toimii ennustettavalla tavalla.

Testit nojaavat silti turhankin paljon toteutusyksityiskohtiin, kuten siihen,
kumpi taulukoista järjestetään ensin.

### Repositoryt

Repositoryjen testausta varten käytetään [testitietokantaa](/src/tests/test_database.py), joka tyhjennetään
ennen jokaista testiä. Tyhjennys tapahtuu repositoryjen omalla `clear()`-metodilla.

### Kuvan lataus

Kuvan latauksessa käytetään eräänlaista mockia emuloimaan PIL-kirjaston `Image`-olioita,
jotta voidaan tarkistaa, skaalattiinko kuva oikealla tavalla.

## Vaatimusten testaus

Vaatimusmäärittelydokumentissa kuvaillut ominaisuudet on testattu manuaalisesti siltä osin,
kuin ne on dokumenttiin merkitty toteutetuiksi.

Käyttöohje on myös käyty läpi kohta kerrallaan manuaalisesti.
