import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def maksukortti(self, saldo=1000):
        return Maksukortti(saldo)

    def test_kassapaate_alustuu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateisosto_rahamaarat_oikein(self):
        paluuarvo = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(paluuarvo, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullinen_kateisosto_kasvattaa_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_kateisosto_liian_vahan_rahaa(self):
        paluuarvo = self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(paluuarvo, 239)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_kateisosto_rahamaarat_oikein(self):
        paluuarvo = self.kassapaate.syo_maukkaasti_kateisella(440)
        self.assertEqual(paluuarvo, 40)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukas_kateisosto_kasvattaa_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(440)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_kateisosto_liian_vahan_rahaa(self):
        paluuarvo = self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(paluuarvo, 399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_korttiosto_riittavasti_rahaa(self):
        kortti = self.maksukortti()
        paluuarvo = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(paluuarvo, True)
        self.assertEqual(str(kortti), "saldo: 7.6")

    def test_edullinen_korttiosto_kasvattaa_myytyjen_maaraa(self):
        kortti = self.maksukortti()
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_korttiosto_ei_riittavasti_rahaa(self):
        kortti = self.maksukortti(239)
        paluuarvo = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(paluuarvo, False)
        self.assertEqual(str(kortti), "saldo: 2.39")
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullinen_kortti_osto_ei_muuta_kassan_rahamaaraa(self):
        kortti = self.maksukortti()
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_korttiosto_riittavasti_rahaa(self):
        kortti = self.maksukortti()
        paluuarvo = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(paluuarvo, True)
        self.assertEqual(str(kortti), "saldo: 6.0")

    def test_maukas_korttiosto_kasvattaa_myytyjen_maaraa(self):
        kortti = self.maksukortti()
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_korttiosto_ei_riittavasti_rahaa(self):
        kortti = self.maksukortti(399)
        paluuarvo = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(paluuarvo, False)
        self.assertEqual(str(kortti), "saldo: 3.99")
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukas_kortti_osto_ei_muuta_kassan_rahamaaraa(self):
        kortti = self.maksukortti()
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataus_positiivisella_toimii(self):
        kortti = self.maksukortti()
        self.kassapaate.lataa_rahaa_kortille(kortti, 550)
        self.assertEqual(str(kortti), "saldo: 15.5")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100550)

    def test_kortin_lataus_negatiivisella_ei_toimi(self):
        kortti = self.maksukortti()
        # pankkiryöstö
        self.kassapaate.lataa_rahaa_kortille(kortti, -50000)
        self.assertEqual(str(kortti), "saldo: 10.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
