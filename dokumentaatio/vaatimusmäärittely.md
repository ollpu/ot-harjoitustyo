# Vaatimusmäärittely

## Käyttötarkoitus

Sovellus on leikki-ikäiselle suunnattu työkalu lukemisen harjoitteluun. Pelaajalle
näytetään erilaisia sanoja, jotka on tarkoitus yhdistää oikeisiin kuviin. Huoltaja
voi lisätä peliin omia tehtäviä.

## Käyttäjät

Sovellusta voi käyttää tekemällä valmiiksi määriteltyjä tehtäviä. Tämän lisäksi
voidaan siirtyä "editointitilaan", jossa huoltaja voi lisätä ja muokata näitä tehtäviä.

## Toiminnallisuus

### Alkuruutu

Alussa valitaan peli, jota halutaan pelata. Pelejä voi siis olla määriteltynä monta.

Peli esitellään sen nimellä ja muutamalla siihen liittyvällä kuvalla, jotta
pelaajakin pystyy valitsemaan mieleisen.

Editointitilaan pääsee alkuruudusta jotenkin, kuitenkin niin ettei pelaaja eksy sinne
vahingossa.

*(tehty: Minkä tahansa pelin voi valita pelattavaksi tai muokattavaksi aloitusruudusta,
mutta editointitilaa ei ole piilotettu)*

### Pelaaminen

Peli etenee tehtävä kerrallaan. Kun yksi tehtävä valmistuu, siirrytään seuraavaan. *(tehty)*
Tehtävät voidaan esittää sattumanvaraisessa järjestyksessä.

Ensisijaisessa tehtävätyypissä pelaajalle esitetään joukko kuvia, ja yksi sana
kerrallaan. Pelaajan on jokaisen sanan kohdalla tarkoitus painaa sitä vastaavaa kuvaa.
Jos painetaan oikein, tehdään tämä ilmeiseksi ja siirrytään hetken päästä seuraavaan sanaan.
*(tehty)*

Jos taas painetaan väärin, tehdään tämä ilmeiseksi ja annetaan pelaajan yrittää uudestaan.
Jossain vaiheessa voidaan siirtyä seuraavaan sanaan, jos sana ei millään mene oikein.
*(tehty)*

Koska pelaaja ei oikein osaa vielä lukea, tulee hyödyntää yksinkertaisia visuaalisia
merkkejä tai ehkä äänimerkkejä.
*(tehty: oikea vastaus on vihreä, väärä vastaus on punainen)*

### Editointitila

Editointitilassa on valittava ensin peli, jota muokataan, tai luoda uusi peli. *(tehty)*

Peli koostuu monesta tehtävästä, joissa jokaisessa on joukko kuva-sana -pareja.
Pelille annetaan myös nimi. *(tehty)*

Kun muokattava kierros on valittu, voidaan siihen lisätä tai poistaa näitä pareja,
sekä muokata sanoja. Uutta paria lisättäessä aukeaa ainakin alustavasti
tiedostonvalintaikkuna, eli kuvaksi tulee valita kuvatiedosto tietokoneelta. *(tehty)*

Luodut pelit tallennetaan käyttäjän tietokoneelle, eli ne eivät katoa kun sovellus
suljetaan. *(tehty)*

## Jatkokehitysideoita

- Erilaisia tehtävätyyppejä, esimerkiksi:
  - Yhden sanan sijasta näytetään vain yksi kuva kerrallaan, ja kaikki sanat
    valmiiksi. Tämä on hieman hankalampi kuin toisin päin.
  - Tehtävän yhteyteen voi myös äänittää puhutun version sanasta. Tällöin puhe
    pitää yhdistää oikeaan sanaan.
  - Kirjoittamiseen liittyviä tehtäviä.
- Kuvien haku jostakin CC-kuvahausta helpottamaan tehtävien laatimista.
- Pelien vieminen ja tuominen, jotta niitä voidaan siirtää toiselle tietokoneelle.
