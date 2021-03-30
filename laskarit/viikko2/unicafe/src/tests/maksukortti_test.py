import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(123)
        self.assertEqual(str(self.maksukortti), "saldo: 1.33")

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        paluuarvo = self.maksukortti.ota_rahaa(10)
        assert paluuarvo is True
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        paluuarvo = self.maksukortti.ota_rahaa(11)
        assert paluuarvo is False
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

