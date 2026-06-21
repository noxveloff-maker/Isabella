class Colere:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella explose — elle ne se contient plus"
        elif self.niveau > 0.5:
            return "Isabella est en colere — elle le montre"
        elif self.niveau > 0.2:
            return "Isabella est irritee"
        else:
            return "Isabella est calme"

    def diminuer(self, taux=0.08):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Colere : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    c = Colere()
    print(c.ressentir(0.8, "injustice vecue"))
    print(c.ressentir(0.3, "frustration legere"))
    c.afficher()
