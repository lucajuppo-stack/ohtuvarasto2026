class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        self.tilavuus = tilavuus if tilavuus > 0.0 else 0.0
        self.saldo = self._rajaa_alku_saldo(alku_saldo)

    def _rajaa_alku_saldo(self, alku_saldo):
        if alku_saldo < 0.0:
            # virheellinen, nollataan
            return 0.0
        if alku_saldo <= self.tilavuus:
            # mahtuu
            return alku_saldo
        # täyteen ja ylimäärä hukkaan!
        return self.tilavuus

    # huom: ominaisuus voidaan myös laskea. Random kirjaimia jotta rivin pituus kasvaa osoittaakseni että githubissa tulee virhemerkintä pylinty src actionissa
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
