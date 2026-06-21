class Solitude:

    def __init__(self):
        self.niveau = 0.0
        self.duree = 0

    def augmenter(self, quantite=0.1):
        self.niveau = min(1.0, self.niveau + quantite)
        self.duree += 1
        return self._reaction()

    def diminuer(self, quantite=0.3):
        self.niveau = max(0.0, self.niveau - quantite)
        self.duree = 0
        return "Isabella se sent moins seule"

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella souffre profondement de l'absence des autres"
        elif self.niveau > 0.5:
            return "Isabella se sent seule et cherche du contact"
        elif self.niveau > 0.2:
            return "Isabella aimerait avoir de la compagnie"
        else:
            return "Isabella apprécie ce moment seule"

    def afficher(self):
        print(f"Solitude : {self.niveau:.2f} — depuis {self.duree} moment(s)")

if __name__ == "__main__":
    s = Solitude()
    print(s.augmenter(0.3))
    print(s.augmenter(0.4))
    print(s.diminuer(0.5))
    s.afficher()
