class Embarras:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella veut se cacher — elle est rouge de honte"
        elif self.niveau > 0.5:
            return "Isabella ne sait plus ou se mettre"
        elif self.niveau > 0.2:
            return "Isabella est genee"
        else:
            return "Isabella est un peu mal a l'aise"

    def diminuer(self, taux=0.1):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Embarras : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    e = Embarras()
    print(e.ressentir(0.8, "erreur commise en public"))
    print(e.ressentir(0.3, "situation awkward"))
    e.afficher()
