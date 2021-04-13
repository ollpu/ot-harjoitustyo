# Ohjelmistotekniikka harjoitustyö

## Dokumentaatio

[Vaatimusmäärittely](/dokumentaatio/vaatimusmäärittely.md)  
[Tuntikirjanpito](/dokumentaatio/tuntikirjanpito.md)  

## Käyttö

Asenna riippuvuudet ja käynnistä sovellus näin:

```sh
poetry install
poetry run invoke start
```

 - Testien ajaminen: `poetry run invoke test`
 - Testikattavuusraportti `htmlcov`-kansioon: `poetry run invoke coverage-report`
 - Pylint: `poetry run invoke lint`

