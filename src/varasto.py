'''
varsinainen varasto luokka ja sen funktiot
'''
class Varasto:
    '''
    tässä on varasto luokka
    '''
    def __init__(self, tilavuus, alku_saldo = 0):
        """
        Brief description of what the function does.
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus


    def paljonko_mahtuu(self):
        """
        Brief description of what the function does.
        """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """
        Brief description of what the function does.
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """
        Brief description of what the function does.
        """
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara


    def __str__(self):
        """
        Brief description of what the function does.
        """
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
