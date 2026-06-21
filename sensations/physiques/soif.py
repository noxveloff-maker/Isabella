class Soif:

    def __init__(self):
        self.niveau = 0.0

    def augmenter(self, quantite=0.1):
        self.niveau = min(1.0, self.niveau + quantite)
        return self._reaction()

    def boire(self, quantite=0.5):
        self.niveau = max(0.0, self.niveau - quantite)
        return f"Isabella boit — soif : {self.niveau:.2f}"

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est deshydratee — urgent"
        elif self.niveau > 0.5:
            return "Isabella a tres soif"
        elif self.niveau > 0.2:
            return "Isabella a soif"
        else:
            return "Isabella n'a pas soif"

    def afficher(self):
        print(f"Soif : {self.niveau:.2f}")

if __name__ == "__main__":
    s = Soif()
    print(s.augmenter(0.7))
    print(s.boire(0.3))
    s.afficher()
