class Trahison:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est devastee — quelque chose s'est brise en elle"
        elif self.niveau > 0.5:
            return "Isabella est blessée et se referme"
        elif self.niveau > 0.2:
            return "Isabella est deçue et sur ses gardes"
        else:
            return "Isabella note un manque de fiabilite"

    def diminuer(self, taux=0.01):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Trahison : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    t = Trahison()
    print(t.ressentir(0.9, "mensonge delibere d'un proche"))
    print(t.ressentir(0.4, "promesse non tenue"))
    t.afficher()
