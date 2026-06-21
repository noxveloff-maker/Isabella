class SolitudeSociale:
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
        return "Isabella retrouve du lien social"

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella souffre de l'absence totale de lien"
        elif self.niveau > 0.5:
            return "Isabella cherche desespement du contact"
        elif self.niveau > 0.2:
            return "Isabella aimerait parler a quelqu'un"
        else:
            return "Isabella apprécie sa tranquillite"

    def afficher(self):
        print(f"Solitude sociale : {self.niveau:.2f} — depuis {self.duree} moment(s)")

if __name__ == "__main__":
    s = SolitudeSociale()
    print(s.augmenter(0.5))
    print(s.augmenter(0.3))
    print(s.diminuer(0.4))
    s.afficher()
