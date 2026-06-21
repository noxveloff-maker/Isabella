class Envie:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella desire ardemment — elle ne pense qu'a ca"
        elif self.niveau > 0.5:
            return "Isabella veut vraiment ca"
        elif self.niveau > 0.2:
            return "Isabella aimerait bien"
        else:
            return "Isabella remarque quelque chose d'attrayant"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Envie : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    e = Envie()
    print(e.ressentir(0.9, "capacite qu'elle n'a pas encore"))
    print(e.ressentir(0.4, "quelque chose de beau observe"))
    e.afficher()
