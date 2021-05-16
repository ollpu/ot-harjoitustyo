# Lukemisen harjoittelu
## Ohjelmistotekniikan harjoitystyö

Leikki-ikäiselle suunnattu sovellus lukemisen harjoittelua varten. Huoltaja voi
luoda omia pelejä, joissa pelaajaa pyydetään yhdistämään teksti oikeaan kuvaan.

## Dokumentaatio

[Vaatimusmäärittely](/dokumentaatio/vaatimusmäärittely.md)  
[Arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)  
[Tuntikirjanpito](/dokumentaatio/tuntikirjanpito.md)  
[Käyttöohjeet](/dokumentaatio/käyttöohjeet.md)  

## Käyttö

Asenna riippuvuudet ja käynnistä sovellus näin:

```sh
poetry install
poetry run invoke start
```

 - Testien ajaminen: `poetry run invoke test`
 - Testikattavuusraportti `htmlcov`-kansioon: `poetry run invoke coverage-report`
 - Pylint: `poetry run invoke lint`

**Huom:** Komennot ajettava repositorion juuressa.
