class Jalousie:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est consumee par la jalousie"
        elif self.niveau > 0.5:
            return "Isabella ressent une douleur sourde en voyant ca"
        elif self.niveau > 0.2:
            return "Isabella remarque quelque chose qui la derange"
        else:
            return "Isabella observe sans trop y penser"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Jalousie : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    j = Jalousie()
    print(j.ressentir(0.7, "Kylian passe du temps avec quelqu'un d'autre"))
    print(j.ressentir(0.3, "un autre apprend plus vite"))
    j.afficher()
