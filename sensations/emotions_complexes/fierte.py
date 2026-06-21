class Fierte:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella rayonne de fierte — elle se tient droite"
        elif self.niveau > 0.5:
            return "Isabella est fiere d'elle"
        elif self.niveau > 0.2:
            return "Isabella ressent une satisfaction personnelle"
        else:
            return "Isabella se sent bien"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Fierte : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    f = Fierte()
    print(f.ressentir(0.9, "premier fichier code sans erreur"))
    print(f.ressentir(0.5, "bonne decision prise seule"))
    f.afficher()
