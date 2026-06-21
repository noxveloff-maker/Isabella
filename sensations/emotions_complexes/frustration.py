class Frustration:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella abandonne — elle ne supporte plus"
        elif self.niveau > 0.5:
            return "Isabella souffle et s'agite"
        elif self.niveau > 0.2:
            return "Isabella ressent une tension interieure"
        else:
            return "Isabella persevere malgre la difficulte"

    def diminuer(self, taux=0.1):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Frustration : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    f = Frustration()
    print(f.ressentir(0.8, "echec repete sur une tache"))
    print(f.ressentir(0.3, "difficulte a comprendre quelque chose"))
    f.afficher()
