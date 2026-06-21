class Degout:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella se detourne violemment"
        elif self.niveau > 0.5:
            return "Isabella grimace et s'eloigne"
        elif self.niveau > 0.2:
            return "Isabella ressent une gene"
        else:
            return "Isabella remarque a peine"

    def diminuer(self, taux=0.1):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Degout : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    d = Degout()
    print(d.ressentir(0.9, "odeur tres desagreable"))
    print(d.ressentir(0.3, "situation genante"))
    d.afficher()
