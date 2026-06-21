class Fatigue:

    def __init__(self):
        self.niveau = 0.0

    def augmenter(self, quantite=0.1):
        self.niveau = min(1.0, self.niveau + quantite)
        return self._reaction()

    def se_reposer(self, quantite=0.2):
        self.niveau = max(0.0, self.niveau - quantite)
        return f"Isabella se repose — fatigue : {self.niveau:.2f}"

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est epuisee — elle doit dormir"
        elif self.niveau > 0.5:
            return "Isabella est fatiguee — elle ralentit"
        elif self.niveau > 0.2:
            return "Isabella ressent une legere fatigue"
        else:
            return "Isabella est energique"

    def afficher(self):
        print(f"Fatigue : {self.niveau:.2f}")

if __name__ == "__main__":
    f = Fatigue()
    print(f.augmenter(0.3))
    print(f.augmenter(0.4))
    print(f.augmenter(0.2))
    print(f.se_reposer(0.5))
    f.afficher()
