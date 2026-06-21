class Confiance:
    def __init__(self):
        self.niveau = 0.5
        self.historique = []

    def renforcer(self, intensite, source):
        self.niveau = min(1.0, self.niveau + intensite)
        self.historique.append({"type": "renforcement", "source": source})
        return self._reaction()

    def affaiblir(self, intensite, source):
        self.niveau = max(0.0, self.niveau - intensite)
        self.historique.append({"type": "affaiblissement", "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella fait totalement confiance"
        elif self.niveau > 0.5:
            return "Isabella fait confiance globalement"
        elif self.niveau > 0.2:
            return "Isabella est prudente"
        else:
            return "Isabella se mefie"

    def afficher(self):
        print(f"Confiance : {self.niveau:.2f}")

if __name__ == "__main__":
    c = Confiance()
    print(c.renforcer(0.3, "Kylian tient sa promesse"))
    print(c.affaiblir(0.2, "deception legere"))
    print(c.renforcer(0.4, "Kylian la protege"))
    c.afficher()
