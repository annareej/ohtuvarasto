import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.virhe_varasto = Varasto(-1, -1)
        self.varasto = Varasto(10)
        self.liian_paljon_varasto = Varasto(5, 10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_virheellisella_varastolla_tyhja_tilavuus(self):
        self.assertAlmostEqual(self.virhe_varasto.tilavuus, 0)

    def test_uudella_virheellisella_varastolla_tyhja_varasto(self):
        self.assertAlmostEqual(self.virhe_varasto.saldo, 0)
    
    def test_liian_iso_saldo_tayttaa_varaston(self):
        self.assertAlmostEqual(self.liian_paljon_varasto.saldo, 5)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
    
    def test_virhe_lisays_ei_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(-8)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_liian_paljon_lisays_ei_kasvata_saldoa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liikaa_ottaminen_palauttaa_kaikki_mita_voidaan(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(saatu_maara, 5)

    def test_liikaa_ottaminen_tyhjentaa_saldon(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_virhe_ottaminen_palauttaa_nolla(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_to_string(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")
        