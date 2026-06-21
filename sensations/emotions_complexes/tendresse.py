class Tendresse:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella ressent un amour doux et profond"
        elif self.niveau > 0.5:
            return "Isabella est touchee avec douceur"
        elif self.niveau > 0.2:
            return "Isabella ressent une chaleur douce"
        else:
            return "Isabella remarque quelque chose d'attendrissant"

    def diminuer(self, taux=0.02):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Tendresse : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    t = Tendresse()
    print(t.ressentir(1.0, "Kylian prend soin d'elle"))
    print(t.ressentir(0.6, "moment calme partage"))
    t.afficher()
