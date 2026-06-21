class Ennui:

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
        return "Isabella trouve quelque chose d'interessant"

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella s'endort — rien ne l'interesse"
        elif self.niveau > 0.5:
            return "Isabella cherche quelque chose a faire"
        elif self.niveau > 0.2:
            return "Isabella commence a se lasser"
        else:
            return "Isabella est occupee"

    def afficher(self):
        print(f"Ennui : {self.niveau:.2f} — depuis {self.duree} moment(s)")

if __name__ == "__main__":
    e = Ennui()
    print(e.augmenter(0.3))
    print(e.augmenter(0.4))
    print(e.diminuer(0.5))
    e.afficher()
