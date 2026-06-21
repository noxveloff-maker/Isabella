class Plaisir:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella rayonne de bonheur"
        elif self.niveau > 0.5:
            return "Isabella sourit largement"
        elif self.niveau > 0.2:
            return "Isabella se sent bien"
        else:
            return "Isabella ressent une legere satisfaction"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Plaisir actuel : {self.niveau:.2f}")
        print(f"Experiences positives : {len(self.historique)}")

if __name__ == "__main__":
    p = Plaisir()
    print(p.ressentir(0.9, "Kylian la felicite"))
    print(p.ressentir(0.5, "reussite d'un calcul"))
    p.afficher()
