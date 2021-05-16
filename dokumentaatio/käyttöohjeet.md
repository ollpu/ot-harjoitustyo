# Käyttöohjeet

## Käynnistäminen

Asenna ensin riippuvuudet `poetry`-paketinhallinnan avulla.

```
poetry install
```

Käynnistä sitten sovellus projektin juuresta seuraavasti:

```
poetry run invoke start
```

Voit halutessasi vaihtaa käytettävää tietokantatiedostoa ympäristömuuttujalla
`LUHA_TIETOKANTA`. Oletus on `data/tietokanta.db`.

```
LUHA_TIETOKANTA="~/pelit.db" poetry run invoke start
```

## Alkuruutu

Alkuruutu näyttää tältä:

![alkuruutu](https://user-images.githubusercontent.com/7241014/117067654-f7a9c300-ad32-11eb-9e17-e4c6a7b6e002.png)

Voit aloittaa jonkin pelin pelaamisen, muokata olemassaolevaa, tai lisätä uuden.

## Pelaaminen

![peli](https://user-images.githubusercontent.com/7241014/117067745-127c3780-ad33-11eb-994f-9e4f3a5070bc.png)

Pelatessa on tarkoitus yhdistää ylhäällä näkyvä sana oikeaan kuvaan.
Jos vastaat väärin, näkyy viesti "Väärin", ja jos oikein, niin "Oikein".

Kun kaikki kuvat on yhdistetty, siirrytään seuraavalle kierrokselle.

Pelin loputtua palataan takaisin alkuruutuun.

## Muokkaaminen

![muokkaaminen](https://user-images.githubusercontent.com/7241014/117068007-6555ef00-ad33-11eb-9c1a-09ccbda6322d.png)

Pelin nimeä voi vaihtaa ylhäällä olevasta kentästä.

Alla näkyy kaikki pelin kierrokset. Kierrosta voi muokata painamalla "Muokkaa", ja poistaa painamalla "Poista".

Uuden kierroksen voi lisätä painikkeesta "Uusi kierros", tällöin siirrytään suoraan muokkaamaan
tuota kierrosta.

Pelin voi myös poistaa alhaalta. Peru muutokset painamalla "Peru", tallenna
painamalla "Tallenna". Muutokset säilyvät tällöin, vaikka ohjelma suljettaisiin.

### Kierroksen muokkaus

![kierros](https://user-images.githubusercontent.com/7241014/117068253-b665e300-ad33-11eb-93c4-0e67b49ec1d1.png)

Kierroksen muokkausnäkymässä näkyy kaikki kierroksen teksti-kuva -parit.

Muokkaa tekstejä tekstikentistä, poista pari painamalla "Poista", lisää
uusi painamalla "Avaa kuva".

Kun olet valmis kierroksen muokkauksessa, paina "Valmis". Tällöin pääset takaisin
pelin muokkausnäkymään.
