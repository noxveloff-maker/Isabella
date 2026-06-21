class Indifference:
    def __init__(self):
        self.niveau = 0.0

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella ne reagit absolument pas"
        elif self.niveau > 0.5:
            return "Isabella hausse les epaules"
        elif self.niveau > 0.2:
            return "Isabella remarque a peine"
        else:
            return "Isabella prête une legere attention"

    def afficher(self):
        print(f"Indifference : {self.niveau:.2f}")

if __name__ == "__main__":
    i = Indifference()
    print(i.ressentir(0.9, "evenement sans importance"))
    print(i.ressentir(0.3, "bruit de fond"))
    i.afficher()
