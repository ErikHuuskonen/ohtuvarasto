'''asdlkjfnalsdfasdflkjns
'''
import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    '''apskjdfakjsldfnlakjsdfna'''
    def setUp(self):
        '''asdljifalaslkdjnfkjsdnf'''
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        '''asdljifalasdlkfjnalsdkjsdnf'''
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        '''asdljifalkjsldfkjgnsdnf'''
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_tilavuus_nollataan(self):
        '''asdljifasoiajdfglkjsdnf'''
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alku_saldo_nollataan(self):
        '''asdljifalkjsdfgsdfgsdnf'''
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_alku_saldo_suurempi_kuin_tilavuus(self):
        '''asdljifaasdlkjsdnf'''
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        '''asdljifalasdfkjsdnf'''
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_pienentaa_vapaata_tilaa(self):
        '''asdljifalasdffdsjsdnf'''
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisaa_negatiivinen_ei_muuta_saldoa(self):
        '''asdljifalsadfkjsdnf'''
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_yli_tilavuuden_tayttaa_varaston(self):
        '''asdljifaasdfasdlkjsdnf'''
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        '''asdljifalkasdfasdjsdnf'''
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        '''asdljifasdfasdfaalkjsdnf'''
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ota_negatiivinen_palauttaa_nolla(self):
        '''asdljifalkjasdfasdfsdnf'''
        saatu_maara = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(saatu_maara, 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ota_yli_saldon_tyhjentaa_varaston(self):
        '''asdljifalkjsdasdfasdfnf'''
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_oikean_merkkijonon(self):
        '''asdljifalkjsdnfasdkfmnasdfasd'''
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")
