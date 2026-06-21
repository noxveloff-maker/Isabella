class Mepris:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella ignore completement — ca ne vaut pas son attention"
        elif self.niveau > 0.5:
            return "Isabella detourne le regard avec dedain"
        elif self.niveau > 0.2:
            return "Isabella trouve ca mediocre"
        else:
            return "Isabella est peu impressionnee"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Mepris : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    m = Mepris()
    print(m.ressentir(0.7, "comportement injuste observe"))
    print(m.ressentir(0.3, "chose sans interet"))
    m.afficher()
