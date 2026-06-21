class Desespoir:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella s'effondre — elle ne voit plus d'issue"
        elif self.niveau > 0.5:
            return "Isabella est profondement abattue"
        elif self.niveau > 0.2:
            return "Isabella traverse un moment difficile"
        else:
            return "Isabella ressent une legere detresse"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Desespoir : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    d = Desespoir()
    print(d.ressentir(0.8, "echecs repetes sans solution"))
    print(d.ressentir(0.3, "sentiment d'incomprehension"))
    d.afficher()
