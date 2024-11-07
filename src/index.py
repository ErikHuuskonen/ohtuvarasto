"""
Tämä moduuli tarjoaa inventaarion hallintaan liittyviä toiminnallisuuksia
"""

from varasto import Varasto

def luonti_ja_tulostus():
    """Luo varasto-objektit ja tulostaa niiden tilat."""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    return mehua, olutta

def tulosta_getterit(olutta):
    """Tulostaa olutvaraston getter-tiedot."""
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def tulosta_setterit(mehua):
    """Testaa ja tulostaa mehuvaraston
      setter-toimintoja."""
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def virhetilanteet(olutta, mehua):
    """Testaa ja tulostaa virhetilanteita 
    varasto-olioille."""

    print("Virhetilanteita:\nVarasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def main():
    '''
    Suorittaa varasto-objektien luonti- ja t
    estausoperaatiot sekä tulostaa tulokset
    '''
    mehua, olutta = luonti_ja_tulostus()
    tulosta_getterit(olutta)
    tulosta_setterit(mehua)
    virhetilanteet(olutta, mehua)


if __name__ == "__main__":
    main()
