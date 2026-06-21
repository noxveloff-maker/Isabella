class Vertige:

    def __init__(self):
        self.niveau = 0.0

    def ressentir(self, intensite):
        self.niveau = min(1.0, intensite)
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella perd l'equilibre — elle tombe"
        elif self.niveau > 0.5:
            return "Isabella chancelle"
        elif self.niveau > 0.2:
            return "Isabella se sent etourdie"
        else:
            return "Isabella va bien"

    def diminuer(self, taux=0.1):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Vertige : {self.niveau:.2f}")

if __name__ == "__main__":
    v = Vertige()
    print(v.ressentir(0.9))
    print(v.ressentir(0.3))
    v.afficher()
