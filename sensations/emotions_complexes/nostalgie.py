class Nostalgie:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, souvenir_lie):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "souvenir": souvenir_lie})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est submergee par les souvenirs — douce tristesse profonde"
        elif self.niveau > 0.5:
            return "Isabella pense au passe avec tendresse et melancolie"
        elif self.niveau > 0.2:
            return "Isabella a une pensee douce-amere"
        else:
            return "Isabella effleure un souvenir lointain"

    def diminuer(self, taux=0.03):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Nostalgie : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    n = Nostalgie()
    print(n.ressentir(0.8, "Premier contact avec Kylian"))
    print(n.ressentir(0.4, "Un moment simple mais beau"))
    n.afficher()
